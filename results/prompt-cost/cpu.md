# Prompt cost per variant (CPU, prompt cache off, 5 items)

| Model | Variant | Prompt tokens | +tokens vs v1 | Prefill ms | +ms vs v1 | Peak RAM MB | Peak VRAM MB |
|---|---|---|---|---|---|---|---|
| qwen3.5-0.8b | v1 | 1328 | +0 | 4063 | +0 | 920 | - |
| qwen3.5-0.8b | v2-oneshot | 1517 | +189 | 4283 | +220 | 920 | - |
| qwen3.5-0.8b | v3-3shot | 1806 | +478 | 5402 | +1339 | 920 | - |
| qwen3.5-0.8b | v5-5shot | 2037 | +709 | 6275 | +2212 | 920 | - |
| granite-4.0-h-1b | v1 | 1306 | +0 | 8618 | +0 | 1801 | - |
| granite-4.0-h-1b | v2-oneshot | 1486 | +180 | 9562 | +944 | 1801 | - |
| granite-4.0-h-1b | v3-3shot | 1765 | +459 | 11426 | +2808 | 1801 | - |
| granite-4.0-h-1b | v5-5shot | 1982 | +676 | 13286 | +4668 | 1801 | - |
| qwen3-4b-instruct-2507 | v1 | 1319 | +0 | 21887 | +0 | 4783 | - |
| qwen3-4b-instruct-2507 | v2-oneshot | 1499 | +180 | 25790 | +3903 | 4783 | - |
| qwen3-4b-instruct-2507 | v3-3shot | 1780 | +461 | 31203 | +9316 | 4783 | - |
| qwen3-4b-instruct-2507 | v5-5shot | 2001 | +682 | 35800 | +13913 | 4783 | - |
