import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs';
import { join, relative, sep } from 'node:path';

const root = process.cwd();
const skillsRoot = join(root, 'skills');
const errors = [];
const namePattern = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
const requiredDirs = ['assets', 'references', 'scripts'];

function fail(path, message) { errors.push(`${relative(root, path)}: ${message}`); }
function filesFlat(dir) {
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) fail(join(dir, entry.name), 'assets/references/scripts must be flat');
  }
}
function referencedPaths(body) {
  return [...body.matchAll(/`((?:assets|references|scripts)\/[A-Za-z0-9._/-]+)`/g)].map(m => m[1]);
}

if (!existsSync(skillsRoot)) fail(skillsRoot, 'missing skills directory');
else {
  for (const entry of readdirSync(skillsRoot, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const dir = join(skillsRoot, entry.name);
    const skill = join(dir, 'SKILL.md');
    if (!existsSync(skill)) { fail(skill, 'missing SKILL.md'); continue; }
    const text = readFileSync(skill, 'utf8');
    const frontmatter = text.match(/^---\n([\s\S]*?)\n---\n/);
    if (!frontmatter) { fail(skill, 'missing YAML frontmatter'); continue; }
    const name = frontmatter[1].match(/^name:\s*(.+)$/m)?.[1]?.trim();
    const description = frontmatter[1].match(/^description:\s*(.+)$/m)?.[1]?.trim();
    if (!name || !description) fail(skill, 'frontmatter requires name and description');
    if (name !== entry.name) fail(skill, `name '${name}' must match directory '${entry.name}'`);
    if (name && !namePattern.test(name)) fail(skill, 'name must use lowercase letters, numbers, and single hyphens');
    if (description && description.length > 1024) fail(skill, 'description exceeds 1024 characters');
    if (text.split('\n').length > 500) fail(skill, 'SKILL.md exceeds 500 lines');
    if (!/^## Error Handling$/m.test(text)) fail(skill, 'missing Error Handling section');
    for (const child of requiredDirs) {
      const childPath = join(dir, child);
      if (!existsSync(childPath) || !statSync(childPath).isDirectory()) fail(childPath, `missing ${child}/ directory`);
      else filesFlat(childPath);
    }
    const body = text.slice(frontmatter[0].length);
    for (const ref of referencedPaths(body)) {
      if (ref.includes('\\') || ref.split('/').includes('..')) fail(skill, `unsafe relative path '${ref}'`);
      else if (!existsSync(join(dir, ref))) fail(skill, `referenced path does not exist: ${ref}`);
    }
  }
}
if (errors.length) { console.error(`SKILL VALIDATION FAILED (${errors.length})\n${errors.join('\n')}`); process.exit(1); }
console.log('SKILL VALIDATION PASSED: all skill metadata, structure, and local references are valid.');
