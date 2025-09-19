// ./src/js/module.js
import Alpine from "alpinejs"
import HTMX from "htmx.org"
import HC from "highcharts"
import DT from "datatables.net-dt"

window.Alpine = Alpine
window.HTMX = HTMX
window.HC = HC
window.DT = DT

import {createIcons, icons} from "lucide"
createIcons({icons})