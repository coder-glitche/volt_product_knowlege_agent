# Copy Plugin

# ✅ Product Requirements Document: Volt Copy Assistant (Figma Plugin)

## 📌 Overview

**Volt Copy Assistant** is a Figma plugin for designers and product managers working on the Volt Money app. It helps improve UX copy across product flows by offering tone-corrected, compliant, and user-friendly rewrites using Google Gemini's AI API — directly within Figma.

---

## 🎯 Core Objectives

- Improve fintech UX copy with tone-aligned suggestions
- Reduce copywriting guesswork for product designers
- Ensure consistency with Volt's design principles (Clarity, Helpfulness, Simplicity, Transparency, Accessibility)
- Save time by suggesting, editing, and replacing copy inside Figma

---

## 🧩 Plugin Actions

### 🔹 When a text layer is selected:

- Show the original text in an editable input box
- Let the user select a tone or context (e.g., CTA, Error, Tooltip, Instructional)
- On clicking “Suggest Rewrite”, send the text + tone to Gemini API
- Show AI-generated suggestion in a preview area
- Allow one-click replacement of the Figma text layer with the suggestion

### 🔸 When **no text layer is selected**:

- Show a clear message: “Please select a text layer to get started”
- Disable suggestion and replace buttons

---

## 💡 Key Features

| Feature | Description |
| --- | --- |
| **Text input** | Auto-populated from selected Figma text layer |
| **Tone/context selector** | Dropdown to choose tone (e.g., Clear & Formal, Conversational, Empathetic) |
| **Suggest button** | Triggers Gemini API call and returns rewrites |
| **Preview suggestion** | Displays new copy in plugin UI |
| **Replace button** | Replaces selected layer’s text with suggested rewrite |
| **Fallback logic** | If Gemini fails, show “Something went wrong. Please try again.” |

---

## 🧱 UI Layout (Plugin Panel)

| Section | Description |
| --- | --- |
| Header | “Volt Copy Assistant” with logo (optional) |
| Original Text | Textarea (pre-filled from selected layer) |
| Context Selector | Dropdown: Error, CTA, Tooltip, Instruction |
| Suggest Button | Click to call Gemini |
| Suggestion Output | Textarea showing new UX copy |
| Replace Button | Click to update Figma layer |

---

## 🔌 External APIs & Data

- **Gemini API (Google)**
    
    `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent`
    
    Authentication via API Key: AIzaSyANJ1RcD5FBIAzxndjvjkZdcmjWDJxl2OA
    
- **Prompt Template (example):**
    
    `"You're a UX writer for an Indian fintech app. Rewrite the following copy in Indian English. Tone: {{context}}. Text: '{{originalText}}'"`
    

---

## 🛡️ Error Handling & Edge Cases

| Scenario | Expected Behavior |
| --- | --- |
| No text layer selected | Show warning, disable actions |
| API call fails | Show “Something went wrong. Please try again.” |
| Suggestion is empty/null | Show fallback: “No suggestion returned.” |
| User clicks replace with no suggestion | Show message: “Please generate a suggestion first.” |

---

## 🛠️ Technical Stack & Files

| File | Purpose |
| --- | --- |
| `manifest.json` | Plugin setup: name, main script, network access |
| `code.js` | Figma-side logic: handle layer selection and text edits |
| `ui.html` | UI panel inside Figma |
| `ui.js` | UI logic: event handling, Gemini fetch, DOM updates |

---

## 🧪 Testing & Usage

1. Open Figma desktop
2. Go to Plugins → Development → Import Plugin from Manifest
3. Select plugin folder (containing `manifest.json`)
4. Run the plugin → select a text layer
5. Choose a tone → click “Suggest Rewrite”
6. View suggestion → click “Replace Text” if satisfied

---

## 🧭 Notes for Cursor Team

- User is a first-time developer and will build this iteratively
- Code must be clean, documented, and easy to edit
- Start with MVP: suggestion + replace
- Later scopes may include: copy system checker, Gemini temperature control, language switching