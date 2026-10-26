import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";

const scriptsDirectory = import.meta.dir;

export function ensureDependenciesInstalled(): void {
  const manifestPath = join(scriptsDirectory, "package.json");
  const dependencyPath = join(scriptsDirectory, "node_modules", "commander", "package.json");
  const expected = JSON.parse(readFileSync(manifestPath, "utf8")).dependencies.commander;
  if (existsSync(dependencyPath)) {
    const actual = JSON.parse(readFileSync(dependencyPath, "utf8")).version;
    if (actual === expected) return;
  }
  throw new Error(
    'Install the declared dependencies first: run "bun install --frozen-lockfile" in ' +
      scriptsDirectory + '. This helper does not install packages automatically.'
  );
}
