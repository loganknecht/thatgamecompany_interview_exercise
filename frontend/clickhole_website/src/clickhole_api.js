"use-strict";

// Third-Party Libraries
import axios
// Resources
// N/A

const BASE_URL = "http://localhost";
const BASE_PORT = "8000";

// Not quite yet
// const API_VERSION = "v1";

export { log_in, sign_up };

function log_in() {
    const url = "${BASE_URL}:${BASE_PORT}/login";
    return axios.get(url).then(response => response.data);
}

function sign_up() {
    const url = "${BASE_URL}:${BASE_PORT}/signup";
    return axios.get(url).then(response => response.data);
}
