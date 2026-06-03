# JMX Architecture — Interactive Canvas

An interactive educational web-based infographic explaining the internal architecture and operational flow of **Java Management Extensions (JMX)**.

> Target audience: Senior Java Developers who need a deep mental model of the MBean Server lifecycle.

## Live Demo

Open `jmx-canvas/index.html` in a browser, or run the dev server:

```bash
python jmx-canvas/serve.py
```

Then visit `http://localhost:5000`.

## Panels

### Panel 1 — Instrumentation Level
- Four MBean types: **Standard**, **Dynamic**, **Open**, **Model**
- Toggle between **Attribute** (getter/setter) and **Operation** (invokable) contracts with live syntax-highlighted Java code
- MBeanInfo metadata tree (`MBeanAttributeInfo`, `MBeanOperationInfo`, `MBeanNotificationInfo`, `MBeanConstructorInfo`)
- Hover any component to reveal its `javax.management.*` class name

### Panel 2 — Agent Level (The Hub)
- **MBean Server** core registry with live ObjectName → MBean table
- Full 4-step registration sequence (`registerMBean`, `ObjectName`)
- **Internal Notification Bus** with animated `AttributeChangeNotification` and `JMXConnectionNotification` packets

### Panel 3 — Remote Management Level
- External tools: **JConsole**, **VisualVM**, **Custom JMX Client**
- **RMI Connector** and **JMXMP Connector** with JMX service URLs
- **HTTP Adaptor** and **SNMP Adaptor** with distinction callout

## Animations

| Button | Description |
|---|---|
| 🔍 Discovery Flow | Animates a request from JConsole → RMI Connector → MBean Server → MBean |
| 📡 Push Notification Loop | Animates a state-change notification from MBean → Bus → MBean Server → JConsole |

## Tech Stack

- Vanilla HTML/CSS/JS — zero dependencies
- Glassmorphism dark UI, monospace code fonts
- SVG overlay for cross-panel path animations
- Python `http.server` for local serving

## Key Java Classes Referenced

| Component | Interface / Class |
|---|---|
| MBean Server | `javax.management.MBeanServer` |
| Standard MBean | `javax.management.StandardMBean` |
| Dynamic MBean | `javax.management.DynamicMBean` |
| Open MBean | `javax.management.openmbean.OpenMBean` |
| Model MBean | `javax.management.modelmbean.ModelMBean` |
| ObjectName | `javax.management.ObjectName` |
| Notification | `javax.management.Notification` |
| RMI Connector | `javax.management.remote.rmi.RMIConnector` |
| HTTP Adaptor | `com.sun.jdmk.comm.HtmlAdaptorServer` |
| SNMP Adaptor | `com.sun.jdmk.comm.SnmpAdaptorServer` |

