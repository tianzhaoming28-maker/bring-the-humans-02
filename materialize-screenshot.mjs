// Materialize screenshot.png from its embedded single-line base64 payload.
//
// The GitHub snapshot channel used to publish this repository carries UTF-8
// text only, so the PNG also travels as data: screenshot-data.mjs holds the
// whole image on one line (a wrapped payload would swamp the entry's
// authored lines). Running this script restores screenshot.png byte for
// byte:
//
//     node materialize-screenshot.mjs
//
// screenshot.png itself is rendered from source by render_screenshot.py.
import { writeFileSync } from "node:fs";
import { SCREENSHOT_PNG_BASE64 } from "./screenshot-data.mjs";

const bytes = Buffer.from(SCREENSHOT_PNG_BASE64, "base64");
writeFileSync(new URL("./screenshot.png", import.meta.url), bytes);
console.log(`wrote screenshot.png (${bytes.length} bytes)`);
