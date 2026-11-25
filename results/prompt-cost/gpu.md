# Prompt cost per variant (GPU, prompt cache off, 10 items)

| Model | Variant | Prompt tokens | +tokens vs v1 | Prefill ms | +ms vs v1 | Peak RAM MB | Peak VRAM MB |
|---|---|---|---|---|---|---|---|
| qwen3.5-0.8b | v1 | 1326 | +0 | 149 | +0 | 931 | 759.0 |
| qwen3.5-0.8b | v2-oneshot | 1515 | +189 | 126 | -23 | 931 | 759.0 |
| qwen3.5-0.8b | v3-3shot | 1804 | +478 | 145 | -4 | 931 | 759.0 |
| qwen3.5-0.8b | v5-5shot | 2035 | +709 | 159 | +10 | 931 | 759.0 |
| granite-4.0-h-1b | v1 | 1305 | +0 | 290 | +0 | 1230 | 1179.0 |
| granite-4.0-h-1b | v2-oneshot | 1485 | +180 | 269 | -21 | 1230 | 1179.0 |
| granite-4.0-h-1b | v3-3shot | 1764 | +459 | 318 | +28 | 1230 | 1179.0 |
| granite-4.0-h-1b | v5-5shot | 1981 | +676 | 347 | +57 | 1230 | 1179.0 |
| qwen3-4b-instruct-2507 | v1 | 1316 | +0 | 340 | +0 | 2770 | 3191.0 |
| qwen3-4b-instruct-2507 | v2-oneshot | 1496 | +180 | 369 | +29 | 2770 | 3191.0 |
| qwen3-4b-instruct-2507 | v3-3shot | 1777 | +461 | 440 | +100 | 2770 | 3191.0 |
| qwen3-4b-instruct-2507 | v5-5shot | 1998 | +682 | 492 | +152 | 2770 | 3191.0 |
