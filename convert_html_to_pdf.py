diff --git a//dev/null b/convert_html_to_pdf.py
index 0000000000000000000000000000000000000000..e54e2136fc8de8b144b1618e64758f496bef1e6b 100644
--- a//dev/null
+++ b/convert_html_to_pdf.py
@@ -0,0 +1,24 @@
+import argparse
+from pathlib import Path
+import pdfkit
+
+
+def convert_html_to_pdf(source_dir: str, output_dir: str) -> None:
+    src_path = Path(source_dir)
+    out_path = Path(output_dir)
+    out_path.mkdir(parents=True, exist_ok=True)
+    for html_file in src_path.glob('*.html'):
+        pdf_file = out_path / (html_file.stem + '.pdf')
+        pdfkit.from_file(str(html_file), str(pdf_file))
+
+
+def main():
+    parser = argparse.ArgumentParser(description='Convert HTML files in a folder to PDF.')
+    parser.add_argument('source_dir', help='Directory containing HTML files')
+    parser.add_argument('output_dir', help='Directory to store generated PDF files')
+    args = parser.parse_args()
+    convert_html_to_pdf(args.source_dir, args.output_dir)
+
+
+if __name__ == '__main__':
+    main()
