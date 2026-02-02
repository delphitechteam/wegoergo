#!/usr/bin/env python3
"""
Convert all markdown files to HTML with professional styling.
Preserves the original .md files and creates .html versions.
"""

import markdown
import os
from pathlib import Path

# HTML template with professional styling
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}

        .container {{
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}

        h1 {{
            color: #2C5F7C;
            border-bottom: 3px solid #E67E50;
            padding-bottom: 10px;
            margin-top: 0;
            font-size: 2.5em;
        }}

        h2 {{
            color: #2C5F7C;
            margin-top: 2em;
            margin-bottom: 0.5em;
            font-size: 2em;
            border-bottom: 2px solid #eee;
            padding-bottom: 8px;
        }}

        h3 {{
            color: #2C5F7C;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            font-size: 1.5em;
        }}

        h4 {{
            color: #555;
            margin-top: 1.2em;
            margin-bottom: 0.5em;
            font-size: 1.2em;
        }}

        p {{
            margin: 1em 0;
            line-height: 1.8;
        }}

        strong {{
            color: #2C5F7C;
            font-weight: 600;
        }}

        em {{
            color: #666;
        }}

        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Monaco', 'Courier New', monospace;
            font-size: 0.9em;
            color: #E67E50;
        }}

        pre {{
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 20px;
            border-radius: 5px;
            overflow-x: auto;
            line-height: 1.5;
            margin: 1.5em 0;
        }}

        pre code {{
            background: transparent;
            padding: 0;
            color: #f8f8f2;
            font-size: 0.95em;
        }}

        ul, ol {{
            margin: 1em 0;
            padding-left: 2em;
        }}

        li {{
            margin: 0.5em 0;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5em 0;
            background: white;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}

        th {{
            background: #2C5F7C;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: 600;
        }}

        td {{
            padding: 12px;
            border-bottom: 1px solid #eee;
        }}

        tr:hover {{
            background: #f9f9f9;
        }}

        blockquote {{
            border-left: 4px solid #E67E50;
            margin: 1.5em 0;
            padding: 0.5em 1.5em;
            background: #f9f9f9;
            font-style: italic;
            color: #666;
        }}

        hr {{
            border: none;
            border-top: 2px solid #eee;
            margin: 2em 0;
        }}

        a {{
            color: #2C5F7C;
            text-decoration: none;
            border-bottom: 1px solid transparent;
            transition: border-bottom 0.2s;
        }}

        a:hover {{
            border-bottom: 1px solid #2C5F7C;
        }}

        .header-info {{
            background: #E8F4F8;
            padding: 15px 20px;
            border-radius: 5px;
            margin-bottom: 30px;
            border-left: 4px solid #2C5F7C;
        }}

        .header-info p {{
            margin: 0.5em 0;
            color: #555;
            font-size: 0.95em;
        }}

        @media (max-width: 768px) {{
            body {{
                padding: 10px;
            }}

            .container {{
                padding: 20px;
            }}

            h1 {{
                font-size: 2em;
            }}

            h2 {{
                font-size: 1.5em;
            }}

            pre {{
                padding: 15px;
                font-size: 0.85em;
            }}

            table {{
                font-size: 0.9em;
            }}

            th, td {{
                padding: 8px;
            }}
        }}

        @media print {{
            body {{
                background: white;
                max-width: 100%;
            }}

            .container {{
                box-shadow: none;
                padding: 0;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header-info">
            <p><strong>Document:</strong> {filename}</p>
            <p><strong>Generated from:</strong> {source_file}</p>
            <p><strong>WegoErgo Website Redesign Project</strong></p>
        </div>
        {content}
    </div>
</body>
</html>
"""

def convert_md_to_html(md_file_path):
    """Convert a single markdown file to HTML."""
    try:
        # Read the markdown file
        with open(md_file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Convert markdown to HTML
        html_content = markdown.markdown(
            md_content,
            extensions=['extra', 'codehilite', 'tables', 'fenced_code', 'nl2br']
        )

        # Get file info
        file_path = Path(md_file_path)
        filename = file_path.stem
        source_file = file_path.name

        # Extract title (first h1 or use filename)
        title = filename.replace('_', ' ').replace('-', ' ').title()

        # Create full HTML document
        full_html = HTML_TEMPLATE.format(
            title=title,
            filename=filename,
            source_file=source_file,
            content=html_content
        )

        # Create HTML file path (same directory, .html extension)
        html_file_path = file_path.with_suffix('.html')

        # Write HTML file
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(full_html)

        return html_file_path

    except Exception as e:
        print(f"Error converting {md_file_path}: {e}")
        return None

def main():
    """Convert all markdown files in the project."""
    base_dir = Path(__file__).parent

    # Find all .md files (excluding the github folder)
    md_files = []
    for md_file in base_dir.rglob('*.md'):
        if '.github' not in str(md_file):
            md_files.append(md_file)

    print(f"Found {len(md_files)} markdown files to convert...")
    print()

    converted = []
    failed = []

    for md_file in sorted(md_files):
        relative_path = md_file.relative_to(base_dir)
        print(f"Converting: {relative_path}")

        html_file = convert_md_to_html(md_file)

        if html_file:
            converted.append(html_file)
            html_relative = html_file.relative_to(base_dir)
            print(f"  ✓ Created: {html_relative}")
        else:
            failed.append(md_file)
            print(f"  ✗ Failed")
        print()

    # Summary
    print("=" * 70)
    print(f"CONVERSION COMPLETE")
    print("=" * 70)
    print(f"Successfully converted: {len(converted)} files")
    if failed:
        print(f"Failed: {len(failed)} files")
        for f in failed:
            print(f"  - {f.relative_to(base_dir)}")
    print()
    print("All HTML files have been created alongside the original .md files.")

if __name__ == "__main__":
    main()
