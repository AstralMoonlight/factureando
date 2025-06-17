# 🧭 Roadmap del Proyecto - Sistema de Facturación e Inventario

## 🎯 Objetivo General

Desarrollar una alternativa económica y moderna al sistema Bsale, con funcionalidades esenciales de inventario, emisión de boletas/facturas electrónicas integradas con SII, y reportes básicos.

---

## 🚀 Fase 1: MVP (Producto Mínimo Viable)

### ✅ Fundamentos Técnicos

- [x] Elección del stack tecnológico: FastAPI, PostgreSQL, React + Tailwind, Git.
- [x] Configuración del entorno local en Fedora.
- [ ] Inicialización de repositorios (`factureando-backend`, `factureando-frontend`).

### 📦 Backend - FastAPI

- [ ] Crear estructura de proyecto con rutas, modelos y servicios.
- [ ] Modelado de productos y variantes:
  - Producto con variantes (color, talla, talco, marca).
  - SKU y stock por variante.
- [ ] Módulo de ventas:
  - Registrar venta (boleta).
  - Actualizar stock automáticamente.
- [ ] Integración con PostgreSQL usando `SQLAlchemy`.
- [ ] Autenticación de usuario (JWT).
- [ ] Configuración de entornos (`.env` y settings).

### 🧾 Integración con SII

- [ ] Estudio del proceso de certificación.
- [ ] Generación de XML para boletas electrónicas.
- [ ] Firma electrónica avanzada (uso de FEA existente).
- [ ] Conexión con webservice del SII (zeep / requests + certificado).

### 🎨 Frontend - React + Tailwind + shadcn/ui

- [ ] Crear layout base (sidebar, topbar, dashboard).
- [ ] Formulario de venta rápida.
- [ ] CRUD de productos y variantes.
- [ ] Visualización de stock y reportes de ventas básicos.

### 🐘 PostgreSQL

- [ ] Diseño de base de datos inicial.
- [ ] Soporte a múltiples sucursales (opcional para MVP).
- [ ] Soporte a unidades de medida personalizables.

### 📊 Reportes

- [ ] Ventas diarias/semanales/mensuales.
- [ ] Productos más vendidos.
- [ ] Stock bajo alerta.

---

## 🔁 Fase 2: Beta Cerrada (Testeo con negocio familiar)

### 👥 Usuarios

- [ ] Permitir gestión multiusuario (vendedor / administrador).
- [ ] Registro de logs de venta por usuario.

### 📤 Facturación electrónica

- [ ] Pruebas reales con SII (modo certificación).
- [ ] Revisión de errores comunes en la validación.

### 🔐 Seguridad

- [ ] Validación estricta de input.
- [ ] Manejo de errores y fallback si falla conexión con SII.

---

## 📦 Fase 3: Versión de Producción

### 🧭 Escalabilidad

- [ ] Separación en microservicios si escala.
- [ ] Contenerización con Docker (opcional).

### 🌐 Despliegue

- [ ] Despliegue inicial en Railway o Render.
- [ ] Configuración HTTPS y certificados.

### 💳 Monetización

- [ ] Sistema de suscripción mensual (MercadoPago / Webpay).
- [ ] Planes escalables: base ($20.000), avanzado ($30.000+).

---

## 📢 Marketing Local

- [ ] Crear folleto digital para locales en Concepción.
- [ ] Red de contacto con galerías comerciales.
- [ ] Testimonios del primer cliente (negocio familiar).

---

## 🧾 Anexos

- [ ] Documentación técnica (README, OpenAPI schema).
- [ ] Guía paso a paso para onboarding de nuevos clientes.
- [ ] Panel de administración para soporte técnico.

---

## ✏️ Última actualización

`{{fecha_actual}}` - en desarrollo por **Jonathan Isla**.
