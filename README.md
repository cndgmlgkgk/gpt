diff --git a/README.md b/README.md
index f59c6fcdb45ca0027f767fce21ef3be4d6b4df1a..7e2c7731b78901ce8889384f1d3bab67c1f972a0 100644
--- a/README.md
+++ b/README.md
@@ -1,3 +1,15 @@
 # GPT Sample Repository
 
 This is a sample repository to test GitHub access and Codex integration.
+
+## Folder Configuration Server
+
+Run `web_config.py` to start a simple web server that lets you set the HTML
+source folder and the PDF output folder through a browser interface.
+
+```bash
+python web_config.py
+```
+
+Then open `http://localhost:8000` in your browser to configure the folders.
+The configuration is saved to `config.json` in the repository directory.
