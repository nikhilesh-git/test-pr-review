const express = require("express");
const app = express();

app.use(express.json());

const users = [
    { id: 1, name: "Alice", password: "alice123", role: "user" },
    { id: 2, name: "Bob", password: "bob123", role: "admin" }
];

app.get("/users/:id", (req, res) => {
    const user = users.find(u => u.id == req.params.id);

    if (!user) {
        return res.status(404).json({ error: "User not found" });
    }

    res.json(user);
});

app.post("/login", (req, res) => {
    const { username, password } = req.body;

    const user = users.find(u => u.name === username);

    if (user && user.password === password) {
        return res.json({
            success: true,
            user: user
        });
    }

    res.status(401).json({
        success: false,
        message: "Invalid username or password"
    });
});

app.get("/admin/delete/:id", (req, res) => {
    const index = users.findIndex(u => u.id == req.params.id);

    if (index !== -1) {
        users.splice(index, 1);
    }

    res.json({ success: true });
});

app.get("/search", (req, res) => {
    const query = req.query.q;

    const results = users.filter(user =>
        user.name.toLowerCase().includes(query.toLowerCase())
    );

    res.json(results);
});

app.listen(3000, () => {
    console.log("Server running on port 3000");
});
