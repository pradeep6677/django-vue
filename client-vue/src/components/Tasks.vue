<template>
    <div class="container mx-auto bg-gray-200 rounded-xl shadow border p-8 m-10">
        <div class="tasks_content">
            <h1>Tasks</h1>
            <table>
                <tr>
                    <th>Title</th>
                    <th>Description</th>
                    <th>Action</th>
                </tr>
                <tr v-for="task in tasks" :key="task.id">
                    <td>{{ task.title }}</td>
                    <td>{{ task.description }}</td>
                    <td>
                        <button @click="toggleTask(task)">
                            {{ task.completed ? 'Undo' : 'Complete' }}
                        </button>
                        <button @click="deleteTask(task)">Delete</button>
                    </td>
                </tr>
            </table>
        </div>
        <div class="add_task">
            <form v-on:submit.prevent="submitForm">
                <div class="sm:col-span-3">
                    <label for="first-name" class="block text-sm font-medium leading-6 text-gray-900">First name</label>
                    <div class="mt-2">
                    <input type="text" name="first-name" id="first-name" autocomplete="given-name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                    </div>
                </div>

                <div class="col-span-full">
                    <label for="about" class="block text-sm font-medium leading-6 text-gray-900">Description</label>
                    <div class="mt-2">
                        <textarea v-model="description" rows="2" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                    </div>
                </div>

                <div class="form-group p-2">
                    <label for="description">Description</label>
                    <textarea class="form-control" id="description" ></textarea>
                </div>
                <div class="form-group p-2">
                    <button type="submit">Add Task</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

    export default {
        name: "taskList",
        data() {
            return {
                // tasks
                tasks: [],
                title: '',
                description: ''
            }
        },
        methods: {
            async getData() {
                try {
                    // fetch tasks
                    const response = await axios.get('http://localhost:8000/api/tasks/');
                    // set the data returned as tasks
                    this.tasks = response.data; 
                } catch (error) {
                    // log the error
                    console.log(error);
                }
            },
            async submitForm(){
                try {
                    // Send a POST request to the API
                    const response = await axios.post('http://localhost:8000/api/tasks/', {
                        title: this.title,
                        description: this.description,
                        completed: false
                    });
                    // Append the returned data to the tasks array
                    this.tasks.push(response.data);
                    // Reset the title and description field values.
                    this.title = '';
                    this.description = '';
                } catch (error) {
                    // Log the error
                    console.log(error);
                }
            },
            async toggleTask(task){
                try{

                    // Send a request to API to update the task
                    const response = await axios.put(`http://localhost:8000/api/tasks/${task.id}/`, {
                        completed: !task.completed,
                        title: task.title,
                        description: task.description
                    });

                    // Get the index of the task being updated
                    let taskIndex = this.tasks.findIndex(t => t.id === task.id);

                    // Reset the tasks array with the new data of the updated task

                    this.tasks = this.tasks.map((task) => {
                        if(this.tasks.findIndex(t => t.id === task.id) === taskIndex){
                            return response.data;
                        }
                        return task;
                    });

                }catch(error){

                    // Log any error
                    console.log(error);
                }
            },
            async deleteTask(task){

                // Confirm if one wants to delete the task
                let confirmation = confirm("Do you want to delete this task?"); 

                if(confirmation){
                    try{

                    // Send a request to delete the task
                    const response = await axios.delete(`http://localhost:8000/api/tasks/${task.id}`);
                    console.log(response);

                    // Refresh the tasks
                    this.getData();
                    }catch(error){

                    // Log any error

                    console.log(error)
                    }
                }      
            }
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }
    }
</script>