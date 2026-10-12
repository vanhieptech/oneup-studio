import { CharacterProfileSchema, type CharacterProfile } from "../validation/schema";
import hiep from "./profiles/hiep.json";
import omi from "./profiles/omi.json";

/** Built-in profiles, parsed once and reused across every video/scene (module-level cache). */
const builtIn: CharacterProfile[] = [hiep, omi].map((p) => CharacterProfileSchema.parse(p));

export type ProfileRegistry = ReadonlyMap<string, CharacterProfile>;

export function createRegistry(extra: unknown[] = []): ProfileRegistry {
  const map = new Map<string, CharacterProfile>();
  for (const p of builtIn) map.set(p.id, p);
  for (const raw of extra) {
    const p = CharacterProfileSchema.parse(raw);
    map.set(p.id, p);
  }
  return map;
}

export const defaultRegistry: ProfileRegistry = createRegistry();
