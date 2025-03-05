function temperaturestatus(temperatura = 20) {
    if (temperatura < -10) {
        return "dzaan civia";
    } else if (temperatura >= -10 && temperatura < 0) {
        return "civia";
    } else if (temperatura >= 0 && temperatura < 20) {
        return "chveulebrivia";
    } else if (temperatura >= 20 && temperatura < 30) {
        return "tbila;
    } else {
        return "cxelia";
    }
}

function calculatori(zuka1 = 0, zuka2 = 0, zuka3 = '+') {
    if (zuka3 === "+") {
        return zuka1 + zuka2;
    } else if (zuka3 === "-") {
        return zuka1 - zuka2;
    } else if (zuka3 === "*") {
        return zuka1 * zuka2;
    } else if (zuka3 === "/") {
        if (zuka3 === 0) {
            return "arasworia";
        }
        return zuka1 / zuka2;
    } else {
        return "shecdoma";
    }
}

