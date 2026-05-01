# Aspan Ground Station & IoT Telemetry Interface 🛰️🌍

A comprehensive IoT and Web integrated project designed to receive, process, and visualize telemetry data using **LoRaWAN**, **The Things Network (TTN)**, and custom **LoRa Gateway** solutions. This project bridges the gap between hardware sensor nodes and a modern, cloud-connected web interface.

## System Architecture: LoRaWAN & The Things Network

This project leverages robust IoT communication protocols to ensure real-time data transmission from remote sensors to the web dashboard.

🔗 **[The Things Network (TTN) Integration]**
The backend is seamlessly integrated with The Things Network via Webhooks. Incoming uplink payloads from edge devices are securely tunneled using **Cloudflare Tunnels** directly into the Django backend, parsed, and stored in the PostgreSQL database for real-time visualization.

### Hardware Infrastructure
- **LoRa Modules:** E-32 (UART Wireless Module)
- **Microcontroller:** STM32 Nucleo Board
- **Gateway Protocol:** LoRaWAN infrastructure routing data to TTN.

---

## Sustainable Development Goals 🌍

- **SDG 9 (Industry, Innovation and Infrastructure):** We leverage state-of-the-art IoT infrastructure and LoRaWAN technology to foster innovation in telemetry and digital data collection.
- **SDG 11 (Sustainable Cities and Communities):** By providing a robust data transmission system, we enable smart city applications, agricultural monitoring, and remote environmental sensing.
- **SDG 13 (Climate Action):** Continuous remote monitoring via long-range sensors helps in gathering critical environmental data to combat climate change.

---

## Project Overview 🚀

This repository contains:

1. **Hardware Configuration** - Setup for STM32 Nucleo and E-32 LoRa modules.
2. **Backend API** - Django-based REST API for TTN Webhooks.
3. **Task Queues** - Celery & Redis for asynchronous data processing.
4. **Interactive Web Interface** - Real-time visualization of sensor data.
5. **Containerized Deployment** - Fully dockerized environment with PostgreSQL, Nginx, and Mailpit.

---

## Project Structure 📂

```text
Aspan Website/
├── api/                  # The Things Network (TTN) Webhook endpoints
├── core/                 # Django Main settings
├── mainpage/             # Landing page and UI elements
├── pages/                # App pages (Sales, Dashboard, etc.)
├── simulation/           # Telemetry simulation and visualization tools
├── .env                  # Environment variables
├── docker-compose.yaml   # Multi-container orchestration
├── Dockerfile            # Backend image build instructions
└── requirements.txt      # Python dependencies
```

---

## Gateway & Hardware Setup 📡

To establish the physical connection between the LoRa modules and the Nucleo board:

1. **E-32 to Nucleo Wiring:**
   - **TXD** -> Nucleo **D2**
   - **RXD** -> Nucleo **D8**
   - **VCC** -> Nucleo **3V3**
   - **GND** -> Nucleo **GND**
2. **Mode Selection:** Connect **M0** and **M1** pins of the E-32 module to **GND** to enable normal data transmission mode.

---

## Quick Start ⚙️

### Prerequisites

- Docker and Docker Compose
- Cloudflared (For exposing local webhook to TTN)

### Installation & Deployment

1. **Clone the repository**
```bash
git clone https://github.com/MuhammedKeremDemirbent/Aspan-Website.git
cd Aspan-Website
```

2. **Start the Docker Containers**
We use `docker-compose` to spin up the entire stack including Database, Redis, Celery, and Django.
```bash
docker compose up -d --build
```

3. **Expose Local Server for TTN Webhook**
To receive data from The Things Network on your local machine, start a Cloudflare tunnel:
```bash
cloudflared tunnel --url http://localhost:8001
```
*Copy the generated `https://*.trycloudflare.com` URL and paste it into your TTN Webhook settings, appending `/api/ttn-webhook/` to the end.*

---

## Features ✨

### IoT & Backend
- **Real-Time TTN Webhooks:** Instant data ingestion from LoRaWAN devices.
- **Asynchronous Processing:** Celery workers handle heavy data parsing without blocking the main thread.
- **Caching & Messaging:** Redis acts as a high-performance message broker.

### Web Interface
- **Dynamic Dashboards:** Visualize incoming telemetry data.
- **Device Management:** Track connected end devices via their `device_id`.
- **Database Management:** Integrated pgAdmin interface accessible via port `5050`.

---

## Acknowledgment 🤝

- **The Things Network** - For the global LoRaWAN infrastructure.
- **Django & Celery** - For the robust backend framework.
- **Docker** - For seamless containerization.

---

## Author 👤

**Muhammed Kerem Demirbent**

- GitHub: [MuhammedKeremDemirbent](https://github.com/MuhammedKeremDemirbent)
