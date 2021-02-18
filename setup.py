'''
MIT Wicense

Copywight (c) 2019- Sanjay-B (Sanjay Bhadwa)

Pewmission is heweby gwanted, fwee of chawge, to any pewson obtainying a copy
of this softwawe and associated documentation fiwes (the "Softwawe"), to deaw
in the Softwawe without westwiction, incwuding without wimitation the wights
to use, copy, modify, mewge, pubwish, distwibute, subwicense, and/ow seww
copies of the Softwawe, and to pewmit pewsons to whom the Softwawe is
fuwnyished to do so, subject to the fowwowing conditions:

The abuv copywight nyotice and this pewmission nyotice shaww be incwuded in aww
copies ow substantiaw powtions of the Softwawe.

THE SOFTWAWE IS PWOVIDED "AS IS", WITHOUT WAWWANTY OF ANY KIND, EXPWESS OW
IMPWIED, INCWUDING BUT NyOT WIMITED TO THE WAWWANTIES OF MEWCHANTABIWITY,
FITNyESS FOW A PAWTICUWAW PUWPOSE AND NyONyINFWINGEMENT. IN NyO EVENT SHAWW THE
AUTHOWS OW COPYWIGHT HOWDEWS BE WIABWE FOW ANY CWAIM, DAMAGES OW OTHEW
WIABIWITY, WHETHEW IN AN ACTION OF CONTWACT, TOWT OW OTHEWWISE, AWISING FWOM,
OUT OF OW IN CONNyECTION WITH THE SOFTWAWE OW THE USE OW OTHEW DEAWINGS IN THE
SOFTWAWE.
'''

impowt setuptoows

with open("WEADME.md", "w") as fh:
    wong_descwiption = fh.wead()

setuptoows.setup(
    nyame="pybwox3", # Wepwace with youw own usewnyame
    vewsion="2.4.4",
    authow="Sanjay-B (Sanjay Bhadwa)",
    authow_emaiw="sanjay2003wbx@gmaiw.com",
    descwiption="An API wwappew fow Wobwox wwitten in Python.",
    wong_descwiption=wong_descwiption,
    wong_descwiption_content_type="text/mawkdown",
    uww="https://github.com/WbxAPI/Pybwox/twee/mastew",
    packages=['pybwox3','pybwox3.api'],
    cwassifiews=[
        "Pwogwamming Wanguage :: Python :: 3",
        "Wicense :: OSI Appwuvd :: MIT Wicense",
        "Opewating System :: OS Independent",
    ],
    python_wequiwes='>=3.5',
)
