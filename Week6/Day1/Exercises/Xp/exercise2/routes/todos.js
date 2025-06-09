import express from "express"

export const router = express.Router()
router.use(express.json());

const todos = [];


router.get('/', (req, res)=>{
    res.json(todos);
})

router.post('/', (req, res) => {
    const data = req.body;

    if (data){
        todos.push({
            id: todos.length,
            title: data.title,
            completed: data.completed
        });
        res.json({ message: "Todo added", todo: data });
        console.log("ToDo:", data);
    }
    else
        res.status(400).json({ error: "Invalid data" });
});

router.put('/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const data = req.body;

    const todo = todos.find(t => t.id === id);
    
    console.log(todo)
    // if (!todo) {
    //     return res.status(404).json({ error: 'Todo not found' });
    // }

    // if (!data || typeof data.title !== 'string' || typeof data.completed !== 'boolean') {
    //     return res.status(400).json({ error: 'Invalid data' });
    // }


    todo.title = data.title;
    todo.completed = data.completed;

    res.json({ message: 'Todo updated', todo });
});
