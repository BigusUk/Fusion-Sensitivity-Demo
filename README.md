# Fusion Yield Sensitivity Scan

"AI and Humanity: Collaborating to Build a Better Future for the Universe."
"These tools aim to help humankind by advancing research in clean energy, life's origins, and cosmic evolution"

This is a highly simplified model; real nuclear resonances are more sensitive—adjust exponent for realism.

## Description
A parameter scan using SymPy and NumPy to test how tiny changes in resonance energy affect fusion yields in the triple-alpha process (hydrogen to carbon in stars).

## Requirements
- Python 3.8+
- sympy
- numpy

## How to Run
1. Install dependencies: `pip install sympy numpy`
2. Save the code as `fusion_sensitivity.py`
3. Run: `python fusion_sensitivity.py`

## Assumptions
- Simplified rate formula: rate = exp(-1000 / E_res) (very steep for demo)
- Variations: ±0.5% in resonance energy.
- Default C/O ratio: 0.6 (observed in universe).


## Example Output
Default C/O ≈ 0.6
-0.5% shift: C/O ≈ 0.004 (drops >99%)
+0.5% shift: C/O ≈ 86.9 (explodes dramatically)

## License
MIT License

Copyright (c) 2025 xAI

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

