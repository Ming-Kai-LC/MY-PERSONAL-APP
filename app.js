class InfiniteMirror {
    constructor() {
        this.canvas = document.getElementById('mirrorCanvas');
        this.ctx = this.canvas.getContext('2d', { willReadFrequently: true });
        this.video = document.getElementById('webcam');
        this.animationId = null;
        this.isRunning = false;

        // Mirror parameters
        this.scale = 0.95;
        this.rotation = 0.5;
        this.depth = 20;
        this.offset = 2;

        this.initializeElements();
        this.setupEventListeners();
    }

    initializeElements() {
        // Set canvas size
        this.canvas.width = 640;
        this.canvas.height = 480;
    }

    setupEventListeners() {
        const startBtn = document.getElementById('startBtn');
        const stopBtn = document.getElementById('stopBtn');
        const scaleSlider = document.getElementById('scaleSlider');
        const rotationSlider = document.getElementById('rotationSlider');
        const depthSlider = document.getElementById('depthSlider');
        const offsetSlider = document.getElementById('offsetSlider');

        startBtn.addEventListener('click', () => this.start());
        stopBtn.addEventListener('click', () => this.stop());

        scaleSlider.addEventListener('input', (e) => {
            this.scale = parseFloat(e.target.value);
            document.getElementById('scaleValue').textContent = this.scale;
        });

        rotationSlider.addEventListener('input', (e) => {
            this.rotation = parseFloat(e.target.value);
            document.getElementById('rotationValue').textContent = this.rotation;
        });

        depthSlider.addEventListener('input', (e) => {
            this.depth = parseInt(e.target.value);
            document.getElementById('depthValue').textContent = this.depth;
        });

        offsetSlider.addEventListener('input', (e) => {
            this.offset = parseFloat(e.target.value);
            document.getElementById('offsetValue').textContent = this.offset;
        });
    }

    async start() {
        try {
            // Request webcam access
            const stream = await navigator.mediaDevices.getUserMedia({
                video: {
                    width: { ideal: 640 },
                    height: { ideal: 480 }
                }
            });

            this.video.srcObject = stream;
            await this.video.play();

            this.isRunning = true;
            document.getElementById('startBtn').disabled = true;
            document.getElementById('stopBtn').disabled = false;

            this.animate();
        } catch (error) {
            console.error('Error accessing webcam:', error);
            alert('Unable to access webcam. Please ensure you have granted camera permissions.');
        }
    }

    stop() {
        this.isRunning = false;

        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
        }

        if (this.video.srcObject) {
            const tracks = this.video.srcObject.getTracks();
            tracks.forEach(track => track.stop());
            this.video.srcObject = null;
        }

        // Clear canvas
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        document.getElementById('startBtn').disabled = false;
        document.getElementById('stopBtn').disabled = true;
    }

    animate() {
        if (!this.isRunning) return;

        // Draw the video frame
        this.ctx.drawImage(this.video, 0, 0, this.canvas.width, this.canvas.height);

        // Create the infinite mirror effect
        this.createMirrorEffect();

        this.animationId = requestAnimationFrame(() => this.animate());
    }

    createMirrorEffect() {
        // Store the current canvas as an image for recursion
        const imageData = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height);

        // Create a temporary canvas to hold the original frame
        const tempCanvas = document.createElement('canvas');
        tempCanvas.width = this.canvas.width;
        tempCanvas.height = this.canvas.height;
        const tempCtx = tempCanvas.getContext('2d');
        tempCtx.putImageData(imageData, 0, 0);

        // Apply recursive mirror effect
        const centerX = this.canvas.width / 2;
        const centerY = this.canvas.height / 2;

        for (let i = 0; i < this.depth; i++) {
            this.ctx.save();

            // Move to center for rotation and scaling
            this.ctx.translate(centerX, centerY);

            // Apply rotation (convert degrees to radians)
            this.ctx.rotate((this.rotation * Math.PI) / 180);

            // Apply scaling
            this.ctx.scale(this.scale, this.scale);

            // Apply offset
            this.ctx.translate(this.offset, this.offset);

            // Move back
            this.ctx.translate(-centerX, -centerY);

            // Draw the canvas onto itself
            this.ctx.globalAlpha = 0.9; // Slight transparency for depth effect
            this.ctx.drawImage(this.canvas, 0, 0);

            this.ctx.restore();
        }
    }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new InfiniteMirror();
});
