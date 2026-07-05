# # CodeAlpha AI Internship - Task 2: Chatbot for FAQs

## Project Description
This repository contains the source architecture for an AI-powered E-Commerce FAQ Customer Support Chatbot built using Botpress Studio. The intelligent agent is tailored for a digital retail platform named **ShopCentral** to streamline client workflows, eliminate manual support ticket queues, and instantly answer core customer inquiries.

Instead of relying on rigid, hard-coded keyword matching, the system employs an **AI-driven NLP text engine**. It reads raw, natural language input directly from the user, evaluates the core intent, and references a strict database of organizational policies to generate a fluid, friendly response.

## Key Features
- **Natural Language Parsing:** Processes raw, human expressions (e.g., "my package hasn't arrived" or "can I get a refund?") rather than requiring exact button clicks.
- **Generative AI Engine:** Dynamically summarizes and formats responses based on 4 foundational store policy pillars:
  1. *Returns Policy:* 30-day return window with 100% free return shipping.
  2. *Shipping Logistics:* Worldwide delivery to 50+ countries within 7-14 business days.
  3. *Order Tracking:* Instant lookup instruction via automated email notification links.
  4. *Secure Checkout:* Multi-channel compliance accepting Credit Cards, Apple Pay, Google Pay, and PayPal.
- **Graceful Fallback Logic:** Autonomously handles user queries outside the store's scope, protecting the conversation loop from breaking and politely redirecting the customer back to valid FAQ options.
- **Endless Interaction Loop:** Resets cleanly to allow multi-tier follow-up questions sequentially.

## File Information
- `CodeAlpha_Chatbot_For_FAQs.bpz`: The full system export file containing all visual node routing layouts, system prompt parameters, and state variable configurations.
