<html>
<body>
<h2>Todo List</h2>
<p>Tâche validée : {{validate_todo}}</p>
<p>Tâche non complète : {{unvalidate_todo}}</p>
    <form action="/todo/add" method="post">
        Task: <input type="text" name="task" />
        <input type="submit" value="Add" />
    </form>
    <ul>
    <!-- Loop through the todos and display them -->
        % for todo in todos:
        <!-- If the todo is completed, display 'Completed', else display 'Not Completed' -->
            <li>{{todo.task}} - {{'Completed' if todo.status else 'Not Completed'}}
                <form action="/todo/update/{{todo.id}}" method="post" style="display:inline;">
                    <input type="checkbox" name="status" {{'checked' if todo.status else ''}} onchange="this.form.submit()" />
                </form>
            </li>
        % end
    </ul>
</body>
</html>