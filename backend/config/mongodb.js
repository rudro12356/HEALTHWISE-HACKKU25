import mongoose from "mongoose";

const connectDB = async () => {
    try {
        // Set up event listeners
        mongoose.connection.on('connected', () => {
            console.log("MongoDB Connected Successfully");
        });

        mongoose.connection.on('error', (err) => {
            console.error("MongoDB Connection Error:", err);
        });

        mongoose.connection.on('disconnected', () => {
            console.log("MongoDB Disconnected");
        });

        // Connect to MongoDB
        await mongoose.connect(process.env.MONGODB_URI, {
            dbName: 'prescripto',
            serverSelectionTimeoutMS: 5000, // Timeout after 5s instead of 30s
            socketTimeoutMS: 45000, // Close sockets after 45s of inactivity
        });

        console.log("MongoDB Connection Initialized");
    } catch (error) {
        console.error("MongoDB Connection Error:", error);
        process.exit(1);
    }
}

export default connectDB;

// Do not use '@' symbol in your databse user's password else it will show an error.