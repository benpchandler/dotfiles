import type { components } from '../types/api.generated';

// Types flow from the backend's Pydantic models → OpenAPI → these generated types.
export type Item = components['schemas']['Item'];
export type HealthResponse = components['schemas']['HealthResponse'];

export async function fetchItems(): Promise<Item[]> {
  const resp = await fetch('/api/items');
  if (!resp.ok) throw new Error(`GET /api/items failed: ${resp.status}`);
  return (await resp.json()) as Item[];
}
