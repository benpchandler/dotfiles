import { describe, expect, it, vi } from 'vitest';
import { fetchItems } from './api';

describe('fetchItems', () => {
  it('returns parsed items on a 200', async () => {
    vi.stubGlobal(
      'fetch',
      vi.fn().mockResolvedValue({
        ok: true,
        json: async () => [{ id: 1, name: 'example', done: false }],
      }),
    );
    const items = await fetchItems();
    expect(items).toHaveLength(1);
    expect(items[0].name).toBe('example');
  });

  it('throws on a non-ok response', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue({ ok: false, status: 500 }));
    await expect(fetchItems()).rejects.toThrow(/500/);
  });
});
