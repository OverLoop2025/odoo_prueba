FROM odoo:16
USER root
RUN pip3 install --no-cache-dir qrcode pillow
RUN mkdir -p /etc/odoo && chown -R odoo:odoo /etc/odoo
USER odoo
