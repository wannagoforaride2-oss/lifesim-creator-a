#!/usr/bin/env python3
"""Generate clean, uniform paper-doll body silhouettes as PNG."""

import cairosvg
from PIL import Image
import io

SKIN_COLOR = '#d2b48f'  # Tan, uniform flat color
OUT_W, OUT_H = 800, 1200  # Consistent output size

def make_svg(outline_path, view_w, view_h):
    """Wrap a path in SVG with transparent bg."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {view_w} {view_h}" width="{view_w}" height="{view_h}">
<path d="{outline_path}" fill="{SKIN_COLOR}" />
</svg>'''

def male_body():
    """Generate male V-taper paper doll silhouette SVG path.
    ViewBox: 400 x 900. Center at x=200.
    Flat tan, no outlines, no shading.
    Body from top of neck (y=10) to feet (y=710).
    """
    # Right-side profile (x off center +), mirrored for left
    cx = 200
    path_parts = []
    
    # Start at top center of neck
    path_parts.append(f'M {cx} 10')
    
    # ── LEFT SIDE (from top to bottom) ──
    # Neck left
    path_parts.append(f'C {cx-8} 10, {cx-14} 14, {cx-16} 22')
    # Shoulder slope out
    path_parts.append(f'C {cx-30} 28, {cx-65} 35, {cx-85} 40')
    # Shoulder curve down
    path_parts.append(f'C {cx-92} 42, {cx-95} 48, {cx-92} 55')
    # Upper arm outer
    path_parts.append(f'C {cx-88} 90, {cx-84} 160, {cx-82} 210')
    # Forearm
    path_parts.append(f'C {cx-80} 260, {cx-78} 300, {cx-74} 320')
    # Hand tip
    path_parts.append(f'C {cx-73} 330, {cx-70} 335, {cx-68} 332')
    # Hand inner (back up arm)
    path_parts.append(f'C {cx-72} 310, {cx-74} 270, {cx-76} 220')
    # Inner arm
    path_parts.append(f'C {cx-78} 170, {cx-80} 110, {cx-82} 80')
    # Armpit
    path_parts.append(f'C {cx-80} 65, {cx-72} 58, {cx-68} 56')
    # Torso side: chest/ribcage
    path_parts.append(f'C {cx-66} 70, {cx-64} 90, {cx-62} 110')
    # Waist (narrow for V-taper)
    path_parts.append(f'C {cx-60} 130, {cx-58} 155, {cx-52} 175')
    # Hip (narrow for male)
    path_parts.append(f'C {cx-50} 195, {cx-52} 210, {cx-54} 230')
    # Upper outer thigh
    path_parts.append(f'C {cx-54} 260, {cx-52} 310, {cx-50} 380')
    # Outer knee
    path_parts.append(f'C {cx-49} 430, {cx-48} 470, {cx-46} 510')
    # Outer calf
    path_parts.append(f'C {cx-44} 560, {cx-42} 610, {cx-40} 660')
    # Outer ankle
    path_parts.append(f'C {cx-39} 685, {cx-40} 700, {cx-46} 710')
    # Left foot bottom (across)
    path_parts.append(f'C {cx-50} 714, {cx-55} 716, {cx-58} 714')
    # Foot inner
    path_parts.append(f'C {cx-56} 710, {cx-52} 705, {cx-50} 700')
    # Inner ankle
    path_parts.append(f'C {cx-48} 690, {cx-46} 660, {cx-44} 630')
    # Inner calf
    path_parts.append(f'C {cx-42} 580, {cx-40} 530, {cx-38} 490')
    # Inner thigh
    path_parts.append(f'C {cx-36} 440, {cx-34} 390, {cx-32} 350')
    # Upper inner thigh
    path_parts.append(f'C {cx-30} 310, {cx-28} 280, {cx-26} 260')
    # Groin/crotch
    path_parts.append(f'C {cx-24} 250, {cx-20} 248, {cx-16} 250')
    # Crotch curve (between legs)
    path_parts.append(f'C {cx-10} 253, {cx-4} 255, {cx} 255')
    # ── RIGHT SIDE (mirror, from bottom to top) ──
    path_parts.append(f'C {cx+4} 255, {cx+10} 253, {cx+16} 250')
    # Right inner thigh up
    path_parts.append(f'C {cx+20} 248, {cx+24} 250, {cx+26} 260')
    path_parts.append(f'C {cx+28} 280, {cx+30} 310, {cx+32} 350')
    path_parts.append(f'C {cx+34} 390, {cx+36} 440, {cx+38} 490')
    path_parts.append(f'C {cx+40} 530, {cx+42} 580, {cx+44} 630')
    path_parts.append(f'C {cx+46} 660, {cx+48} 690, {cx+50} 700')
    # Right foot
    path_parts.append(f'C {cx+52} 705, {cx+56} 710, {cx+58} 714')
    path_parts.append(f'C {cx+55} 716, {cx+50} 714, {cx+46} 710')
    path_parts.append(f'C {cx+40} 700, {cx+39} 685, {cx+40} 660')
    path_parts.append(f'C {cx+42} 610, {cx+44} 560, {cx+46} 510')
    path_parts.append(f'C {cx+48} 470, {cx+49} 430, {cx+50} 380')
    # Right outer thigh up
    path_parts.append(f'C {cx+52} 310, {cx+54} 260, {cx+54} 230')
    # Right hip
    path_parts.append(f'C {cx+52} 210, {cx+50} 195, {cx+52} 175')
    # Right waist
    path_parts.append(f'C {cx+58} 155, {cx+60} 130, {cx+62} 110')
    # Right chest/ribcage
    path_parts.append(f'C {cx+64} 90, {cx+66} 70, {cx+68} 56')
    # Right armpit
    path_parts.append(f'C {cx+72} 58, {cx+80} 65, {cx+82} 80')
    # Inner right arm
    path_parts.append(f'C {cx+80} 110, {cx+78} 170, {cx+76} 220')
    # Right hand inner
    path_parts.append(f'C {cx+74} 270, {cx+72} 310, {cx+68} 332')
    path_parts.append(f'C {cx+70} 335, {cx+73} 330, {cx+74} 320')
    # Right forearm
    path_parts.append(f'C {cx+78} 300, {cx+80} 260, {cx+82} 210')
    # Upper right arm
    path_parts.append(f'C {cx+84} 160, {cx+88} 90, {cx+92} 55')
    # Right shoulder
    path_parts.append(f'C {cx+95} 48, {cx+92} 42, {cx+85} 40')
    path_parts.append(f'C {cx+65} 35, {cx+30} 28, {cx+16} 22')
    # Right neck
    path_parts.append(f'C {cx+14} 14, {cx+8} 10, {cx} 10')
    
    return ' '.join(path_parts), 400, 900


def female_body():
    """Generate female coke-bottle paper doll silhouette SVG path.
    ViewBox: 400 x 900. Center at x=200.
    Flat tan, no outlines, no shading.
    """
    cx = 200
    path_parts = []
    
    # Start at top center of neck
    path_parts.append(f'M {cx} 10')
    
    # ── LEFT SIDE ──
    # Neck left
    path_parts.append(f'C {cx-8} 10, {cx-12} 14, {cx-14} 22')
    # Shoulder (less broad than male)
    path_parts.append(f'C {cx-25} 28, {cx-50} 35, {cx-72} 40')
    # Shoulder curve
    path_parts.append(f'C {cx-78} 42, {cx-82} 48, {cx-78} 55')
    # Upper arm outer
    path_parts.append(f'C {cx-74} 90, {cx-72} 150, {cx-70} 200')
    # Forearm
    path_parts.append(f'C {cx-68} 240, {cx-66} 280, {cx-62} 305')
    # Hand
    path_parts.append(f'C {cx-60} 315, {cx-58} 320, {cx-56} 318')
    # Hand inner
    path_parts.append(f'C {cx-60} 298, {cx-62} 260, {cx-64} 210')
    # Inner arm
    path_parts.append(f'C {cx-66} 160, {cx-68} 100, {cx-70} 80')
    # Armpit
    path_parts.append(f'C {cx-68} 65, {cx-62} 58, {cx-56} 56')
    # Torso: bust area (fuller)
    path_parts.append(f'C {cx-54} 68, {cx-64} 85, {cx-66} 100')
    # Bust curve (moderate)
    path_parts.append(f'C {cx-68} 115, {cx-66} 130, {cx-62} 145')
    # Waist (narrow hourglass)
    path_parts.append(f'C {cx-58} 158, {cx-42} 170, {cx-36} 180')
    # Hip curve out (wide coke-bottle flare)
    path_parts.append(f'C {cx-36} 190, {cx-80} 205, {cx-95} 225')
    # Upper outer thigh (taper from hips)
    path_parts.append(f'C {cx-97} 240, {cx-88} 260, {cx-74} 320')
    # Outer knee
    path_parts.append(f'C {cx-70} 370, {cx-68} 410, {cx-66} 460')
    # Outer calf
    path_parts.append(f'C {cx-64} 510, {cx-62} 560, {cx-58} 620')
    # Outer ankle
    path_parts.append(f'C {cx-56} 660, {cx-54} 690, {cx-46} 710')
    # Left foot
    path_parts.append(f'C {cx-48} 714, {cx-52} 716, {cx-54} 714')
    path_parts.append(f'C {cx-52} 710, {cx-48} 705, {cx-46} 700')
    # Inner ankle
    path_parts.append(f'C {cx-44} 690, {cx-42} 660, {cx-40} 620')
    # Inner calf
    path_parts.append(f'C {cx-38} 560, {cx-36} 510, {cx-34} 460')
    # Inner thigh
    path_parts.append(f'C {cx-32} 400, {cx-30} 350, {cx-28} 310')
    path_parts.append(f'C {cx-26} 280, {cx-24} 260, {cx-20} 250')
    # Crotch curve
    path_parts.append(f'C {cx-14} 248, {cx-7} 250, {cx} 251')
    
    # ── RIGHT SIDE (mirror) ──
    path_parts.append(f'C {cx+7} 250, {cx+14} 248, {cx+20} 250')
    path_parts.append(f'C {cx+24} 260, {cx+26} 280, {cx+28} 310')
    path_parts.append(f'C {cx+30} 350, {cx+32} 400, {cx+34} 460')
    path_parts.append(f'C {cx+36} 510, {cx+38} 560, {cx+40} 620')
    path_parts.append(f'C {cx+42} 660, {cx+44} 690, {cx+46} 700')
    # Right foot
    path_parts.append(f'C {cx+48} 705, {cx+52} 710, {cx+54} 714')
    path_parts.append(f'C {cx+52} 716, {cx+48} 714, {cx+46} 710')
    path_parts.append(f'C {cx+54} 690, {cx+56} 660, {cx+58} 620')
    path_parts.append(f'C {cx+62} 560, {cx+64} 510, {cx+66} 460')
    path_parts.append(f'C {cx+68} 410, {cx+70} 370, {cx+72} 330')
    path_parts.append(f'C {cx+88} 260, {cx+97} 240, {cx+95} 225')
    path_parts.append(f'C {cx+80} 205, {cx+36} 190, {cx+36} 180')
    path_parts.append(f'C {cx+42} 170, {cx+58} 158, {cx+62} 145')
    path_parts.append(f'C {cx+66} 130, {cx+68} 115, {cx+66} 100')
    path_parts.append(f'C {cx+64} 85, {cx+54} 68, {cx+56} 56')
    # Right armpit
    path_parts.append(f'C {cx+62} 58, {cx+68} 65, {cx+70} 80')
    path_parts.append(f'C {cx+68} 100, {cx+66} 160, {cx+64} 210')
    # Right hand
    path_parts.append(f'C {cx+62} 260, {cx+60} 298, {cx+56} 318')
    path_parts.append(f'C {cx+58} 320, {cx+60} 315, {cx+62} 305')
    path_parts.append(f'C {cx+66} 280, {cx+68} 240, {cx+70} 200')
    path_parts.append(f'C {cx+72} 150, {cx+74} 90, {cx+78} 55')
    # Right shoulder
    path_parts.append(f'C {cx+82} 48, {cx+78} 42, {cx+72} 40')
    path_parts.append(f'C {cx+50} 35, {cx+25} 28, {cx+14} 22')
    path_parts.append(f'C {cx+12} 14, {cx+8} 10, {cx} 10')
    
    return ' '.join(path_parts), 400, 900


def render_to_png(path_str, view_w, view_h, output_path, target_w, target_h):
    """Render SVG path to PNG at target resolution."""
    svg_content = make_svg(path_str, view_w, view_h)
    
    # Render to PNG at viewBox resolution via cairosvg
    png_data = cairosvg.svg2png(bytestring=svg_content.encode('utf-8'),
                                output_width=target_w, output_height=target_h)
    
    # Load with PIL and ensure proper format
    img = Image.open(io.BytesIO(png_data))
    # Convert to proper RGBA
    img = img.convert('RGBA')
    img.save(output_path, 'PNG')
    
    # Verify
    loaded = Image.open(output_path)
    print(f'{output_path}: {loaded.size} mode={loaded.mode}')
    
    # Verify uniformity
    pixels = list(loaded.getdata())
    colors = [p for p in pixels if p[3] > 0]
    if colors:
        r_vals = [c[0] for c in colors]
        g_vals = [c[1] for c in colors]
        b_vals = [c[2] for c in colors]
        print(f'  Mean: ({sum(r_vals)//len(r_vals)}, {sum(g_vals)//len(g_vals)}, {sum(b_vals)//len(b_vals)})')
        print(f'  Pixels: {len(colors)} opaque out of {len(pixels)}')
        r_range = max(r_vals) - min(r_vals)
        print(f'  Color range: {r_range} (0 = perfect uniform)')
    
    # Find visible bounds
    w, h = loaded.size
    xmin, xmax, ymin, ymax = w, 0, h, 0
    for y in range(h):
        for x in range(w):
            if loaded.getpixel((x, y))[3] > 10:
                if x < xmin: xmin = x
                if x > xmax: xmax = x
                if y < ymin: ymin = y
                if y > ymax: ymax = y
    
    body_w = xmax - xmin + 1
    body_h = ymax - ymin + 1
    print(f'  Visible bounds: x={xmin}-{xmax}, y={ymin}-{ymax}')
    print(f'  Body size: {body_w}x{body_h}')
    print(f'  Center: ({((xmin+xmax)/2):.1f}, {((ymin+ymax)/2):.1f})')
    
    # Width profile
    for frac in [0.2, 0.35, 0.5, 0.65, 0.8]:
        y = int(ymin + (ymax-ymin)*frac)
        xs = [x for x in range(xmin, xmax+1) if loaded.getpixel((x, y))[3] > 10]
        if xs:
            width = xs[-1] - xs[0]
            ctr = (xs[0] + xs[-1]) / 2
            print(f'    y={frac:.2f}: width={width}px, center={ctr:.1f}')
    
    return img


if __name__ == '__main__':
    import os
    out_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("=== Generating Male Body (V-taper) ===")
    m_path, m_w, m_h = male_body()
    render_to_png(m_path, m_w, m_h, os.path.join(out_dir, 'body.png'), OUT_W, OUT_H)
    
    print()
    print("=== Generating Female Body (Coke bottle) ===")
    f_path, f_w, f_h = female_body()
    render_to_png(f_path, f_w, f_h, os.path.join(out_dir, 'body2.png'), OUT_W, OUT_H)
    
    print()
    print("Done! Both bodies generated at {}x{}".format(OUT_W, OUT_H))