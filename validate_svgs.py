import xml.etree.ElementTree as ET
from pathlib import Path

root = Path('.')
svg_files = list(root.glob('*.svg'))
failed = []
print('Checking', len(svg_files), 'SVG files')
for f in svg_files:
    try:
        ET.parse(f)
        print('OK ', f)
    except ET.ParseError as e:
        print('ERROR', f, '-', e)
        failed.append((f, str(e)))

if failed:
    print('\nSummary: {} file(s) failed'.format(len(failed)))
    for f, e in failed:
        print(f, e)
else:
    print('\nAll SVGs are well-formed XML.')
