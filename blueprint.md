# Blueprint: Tesla & Palantir Stock Tracker

## Overview
A beautifully designed, real-time stock tracking dashboard focused exclusively on Tesla (TSLA) and Palantir (PLTR). It features an elegant dark mode aesthetic with glassmorphism elements, leveraging modern Web Technologies (HTML, CSS, JS) without frameworks.

## Current State & Outline
- **Design:** Modern dark theme with vibrant accents for stock movements (green/red), utilizing subtle noise textures and smooth drop shadows.
- **Technologies:** HTML5, CSS3 (Baseline features, CSS Variables, Flexbox/Grid), Vanilla JavaScript.
- **Data Source:** Real-time financial widgets provided by TradingView (embedded without requiring an API key).
- **Features:** 
  - A top ticker tape displaying current market trends.
  - Interactive Advanced Charts for both TSLA and PLTR.
  - Responsive layout that works perfectly on both desktop and mobile devices.

## Current Plan & Actionable Steps (Tesla & Palantir Tracking)
1. **Scaffold Layout:** Update `index.html` to include a header, a ticker container, and a main grid layout for the stock cards.
2. **Integrate TradingView:** Embed TradingView's Ticker Tape widget and Advanced Chart widgets for TSLA (NASDAQ) and PLTR (NYSE).
3. **Apply Modern Styling:** Update `style.css` with a sleek dark-mode color palette, custom Google Fonts (e.g., Inter), smooth transitions, and responsive container queries.
4. **JavaScript Enhancements:** Use `main.js` to manage any dynamic interactions if necessary (mostly handled by TradingView widgets, but JS can add a clock or greeting).
5. **Deploy & Version Control:** Commit changes and push them automatically to GitHub as requested by the user.

## New Feature: Math Knowledge Graph
- **Purpose:** Visualize the hierarchical relationships between elementary mathematics concepts.
- **Implementation:** 
  - A Python script (`math_graph.py`) uses `networkx` and `matplotlib` to generate a directed graph image (`elementary_math_map.png`).
  - The image is displayed in a new dedicated section on the web dashboard, styled with the same modern dark-mode aesthetic as the stock tracker.
