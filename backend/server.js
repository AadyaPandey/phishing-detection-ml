const express = require('express');
const { exec } = require('child_process');
const cors = require('cors');

const app = express();
const router = express.Router();

// Middleware
app.use(cors());
app.use(express.json());

// API route for prediction
router.post('/api/predict', async (req, res) => {
    const url = req.body.url;

    if (!url) {
        return res.status(400).json({ error: 'URL is required' });
    }

    // Run Python script with the provided URL
    exec(`python python/predictor.py "${url}"`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${error.message}`);
            return res.status(500).json({ error: 'Prediction failed' });
        }

        if (stderr) {
            console.error(`stderr: ${stderr}`);
            return res.status(500).json({ error: 'Python error' });
        }

        const prediction = stdout.trim(); // Expected '0' or '1'
        let label;

        if (prediction === '0') {
            label = 'Legit';
        } else if (prediction === '1') {
            label = 'Phishing';
        } else {
            label = 'Unknown';
        }

        res.json({ result: label, raw: prediction });
    });
});

// Mount router
app.use(router);

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, '0.0.0.0', () => {
    console.log(`✅ Server running on http://localhost:${PORT}`);
});
