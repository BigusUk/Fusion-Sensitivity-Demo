# Fusion Sensitivity Demo

> "AI and Humanity: Collaborating to Build a Better Future for the Universe."

A lightweight Python script demonstrating the extreme sensitivity of stellar carbon production (via the triple-alpha process and the Hoyle state resonance) to very small variations in nuclear resonance energy. This illustrates one of the classic examples of fine-tuning in astrophysics and nuclear physics relevant to the cosmic abundance of carbon and oxygen—elements essential for life.

## Why This Matters
The triple-alpha process converts helium into carbon in stars through a narrow resonance (the Hoyle state). Peer-reviewed studies show that shifts of just ~0.5% in this resonance energy can drastically reduce or explode carbon yields, affecting the cosmic C/O ratio. This demo exaggerates the effect slightly for clarity but faithfully captures the qualitative asymmetry.

## Features
- Uses SymPy and NumPy for clean symbolic/numerical computation
- Avoids numerical underflow/overflow with logarithmic handling
- Shows how a ±0.5% change in resonance energy collapses or explodes the effective C/O ratio
- Fully transparent and educational—explicitly labeled as simplified

## Requirements
- Python 3.8+
- `sympy>=1.12`
- `numpy>=1.24`

Install dependencies:
```bash
pip install sympy numpy

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


