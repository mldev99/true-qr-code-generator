import argparse
import sys
from pathlib import Path
from src.qr_generator import generate_qr

































    main()if __name__ == "__main__":    print(f"Saved QR code to {out_path}")                fill_color=args.fill, back_color=args.back)    generate_qr(data, out_path, box_size=args.box_size, border=args.border,    out_path = args.out        sys.exit(2)        print("No input provided. Use --text or --infile.")    else:        data = args.text    elif args.text:        data = p.read_text(encoding="utf-8")            sys.exit(2)            print(f"Input file not found: {args.infile}", file=sys.stderr)        if not p.exists():        p = Path(args.infile)    if args.infile:    args = parser.parse_args()    parser.add_argument("--back", default="white", help="Background color")    parser.add_argument("--fill", default="black", help="Fill color")    parser.add_argument("--border", type=int, default=4, help="Border boxes")    parser.add_argument("--box-size", type=int, default=10, help="Box pixel size")    parser.add_argument("--out", help="Output PNG path", required=True)    parser.add_argument("--infile", help="Read text from a file (overrides --text)")    parser.add_argument("--text", help="Text or URL to encode", required=False)    parser = argparse.ArgumentParser(description="Generate a QR code PNG")ndef main():