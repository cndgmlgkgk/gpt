diff --git a//dev/null b/web_config.py
index 0000000000000000000000000000000000000000..1db75d622f95523a2c0b97bba991d2e090e3eb9f 100644
--- a//dev/null
+++ b/web_config.py
@@ -0,0 +1,83 @@
+import http.server
+import socketserver
+import urllib.parse
+import json
+import os
+
+CONFIG_FILE = 'config.json'
+
+DEFAULT_CONFIG = {
+    'html_folder': '',
+    'pdf_folder': ''
+}
+
+def load_config():
+    if os.path.exists(CONFIG_FILE):
+        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
+            return json.load(f)
+    return DEFAULT_CONFIG.copy()
+
+
+def save_config(config):
+    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
+        json.dump(config, f)
+
+
+class ConfigHandler(http.server.SimpleHTTPRequestHandler):
+    config = load_config()
+
+    def do_GET(self):
+        if self.path == '/':
+            self.send_response(200)
+            self.send_header('Content-type', 'text/html; charset=utf-8')
+            self.end_headers()
+            self.wfile.write(self.render_form().encode('utf-8'))
+        else:
+            super().do_GET()
+
+    def do_POST(self):
+        if self.path == '/':
+            length = int(self.headers.get('Content-Length', 0))
+            data = self.rfile.read(length)
+            fields = urllib.parse.parse_qs(data.decode('utf-8'))
+            html_folder = fields.get('html_folder', [''])[0]
+            pdf_folder = fields.get('pdf_folder', [''])[0]
+            self.config['html_folder'] = html_folder
+            self.config['pdf_folder'] = pdf_folder
+            save_config(self.config)
+            self.send_response(200)
+            self.send_header('Content-type', 'text/html; charset=utf-8')
+            self.end_headers()
+            self.wfile.write(self.render_form(saved=True).encode('utf-8'))
+        else:
+            self.send_error(404)
+
+    def render_form(self, saved=False):
+        msg = '<p>Configuration saved.</p>' if saved else ''
+        html_folder = self.config.get('html_folder', '')
+        pdf_folder = self.config.get('pdf_folder', '')
+        return f'''
+        <html>
+            <body>
+                <h1>Folder Configuration</h1>
+                {msg}
+                <form method="post" action="/">
+                    <label>HTML Folder:</label>
+                    <input type="text" name="html_folder" value="{html_folder}"><br>
+                    <label>PDF Folder:</label>
+                    <input type="text" name="pdf_folder" value="{pdf_folder}"><br>
+                    <input type="submit" value="Save">
+                </form>
+            </body>
+        </html>
+        '''
+
+
+def run(server_class=http.server.HTTPServer, handler_class=ConfigHandler):
+    with server_class(('localhost', 8000), handler_class) as httpd:
+        print('Serving on http://localhost:8000')
+        httpd.serve_forever()
+
+
+if __name__ == '__main__':
+    run()
