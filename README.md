# Odoo Prueba de trabajo

Este proyecto contiene la configuración completa de Odoo 16 en Docker junto con los módulos desarrollados como parte del examen práctico.  
El entorno está preparado para que pueda ejecutarse directamente, sin necesidad de instalaciones adicionales.

---

## Instalación y ejecución

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/OverLoop2025/odoo_prueba.git
   cd odoo_prueba
   ```

2. Construir y levantar el entorno:
   ```bash
   docker compose up -d --build
   ```

3. Abrir el navegador y acceder a:
   ```
   http://localhost:8069
   ```

4. Crear una nueva base de datos (por ejemplo: `odoo_exam`).

5. En el panel de Odoo:
   - Ir a **Ajustes → Activar modo desarrollador**
   - Entrar a **Aplicaciones → Actualizar lista de aplicaciones**

6. Instalar los módulos:
   - **Exam POS**
   - **Exam Account**
   - **Contactos**
   - **Ventas**
   - **Punto de Ventas**

7. Refrescar el navegador para que se carguen los cambios de interfaz.

---

## Herramientas utilizadas
	•	Odoo 16 Community Edition
	•	Docker y Docker Compose
	•	Ubuntu 22.04 LTS
	•	PostgreSQL 15
	•	Visual Studio Code
	•	Odoo Shell / Terminal Bash
	•	Navegador web (para la interfaz del POS y configuración)

---

## Descripción breve de los módulos

- **Exam POS:**  
  Incluye mejoras visuales y lógicas en el punto de venta, como la columna de idioma en clientes, alerta de precio 0.0 y el botón “Boleta” que muestra el total en un popup.

- **Exam Account:**  
  Agrega la generación de código QR en facturas, maneja serie y correlativo, canal de ventas, fecha de emisión con hora, relación con transferencias (`stock.picking`) y extiende el reporte impreso.

---

## Autor

**Jose Reymundo Alvarez Levano**  
**OverLoop2025**

---