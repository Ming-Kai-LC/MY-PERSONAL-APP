# Infinite Mirror Effect

An interactive web application that creates a mesmerizing infinite mirror effect using your webcam. Experience the visual recursion of a mirror reflecting itself endlessly.

## Features

- Real-time webcam capture with infinite recursive reflection
- Adjustable parameters for customization:
  - **Recursion Scale**: Control how much each reflection shrinks
  - **Rotation**: Add spiral effects to the recursion
  - **Mirror Depth**: Adjust how many recursive layers are rendered
  - **Offset**: Fine-tune the position shift of each reflection
- Smooth 60 FPS animation
- Responsive design that works on desktop and mobile

## How It Works

The app creates an infinite mirror effect by:

1. Capturing video from your webcam
2. Drawing the video frame onto a canvas
3. Recursively drawing the canvas onto itself with transformations (scale, rotate, translate)
4. Each iteration creates a smaller, slightly transformed version of the previous frame
5. The result is a hypnotic infinite regression effect

## Usage

1. Open `index.html` in a modern web browser
2. Click "Start Mirror" and grant camera permissions
3. Adjust the sliders to create different effects:
   - Lower scale values create smaller reflections
   - Higher rotation values create spiral effects
   - More depth creates more recursive layers
   - Offset shifts each reflection spatially
4. Move your hands or objects in front of the camera for a trippy experience
5. Click "Stop Mirror" to pause

## Technical Details

- Pure vanilla JavaScript (no dependencies)
- Uses HTML5 Canvas API for rendering
- WebRTC getUserMedia API for webcam access
- RequestAnimationFrame for smooth animations
- Context transformations for recursive effects

## Browser Requirements

- Modern browser with webcam support (Chrome, Firefox, Safari, Edge)
- WebRTC support for camera access
- HTML5 Canvas support

## Visual Effect Explanation

The infinite mirror effect works similarly to standing between two parallel mirrors. When you draw the canvas onto itself repeatedly with slight transformations:

- Each draw operation captures the previous state
- The transformations (scale + rotation + offset) create the recursion
- The accumulation of these operations creates the infinite tunnel effect
- The alpha transparency adds depth perception

## Tips for Cool Effects

- Set rotation to 0 and scale to 0.95 for a classic tunnel effect
- Increase rotation to 2-3 degrees for a spiral galaxy effect
- Use small offset values (1-3px) for subtle shifts
- Adjust depth based on performance (lower for slower devices)
- Wave your hands in circular motions for flowing patterns

## License

MIT License - Feel free to use and modify as you wish!

## Credits

Created as a demonstration of canvas recursion and webcam integration.
