<template>

<form @submit.prevent="registerUser">
    <h1>Registration </h1>
    <div>
    <label>Username </label>
    <input type="text" v-model="username" required/>
    </div>

    <div>
           <label>Email</label>
    <input type="email" v-model="email" required/>
    </div>

    <div>
        <label>Password</label>
    <input type="password" v-model="password1" required/>
    </div>

    <div>
        <label>Password </label>
    <input type="password" v-model="password2" required/>
    </div>
    <button type="submit"> Submit</button>
</form>
    <p v-if="message"> {{message}}</p>

</template>


<script>
import api from "../axios";

export default{
    data(){
        return{
            username: "",            //stored the username from the input v-model
            email: "",               //stored the username from the input v-model
            password1: "",            //stored the username from the input v-model
            password2: "",            //stored the username from the input v-model
            message: "",                //stored the username from the input v-if

        };
    },
    methods: {
    async registerUser(){ //this will trigger when you click the button
        try{
            const response = await api.post("/auth/registration/", {        //connects to the backend and send data from this API endpoint
                username: this.username,        //send username to th backend
                email: this.email,              //send username to th backend
                password1: this.password1,        //send username to th backend
                password2: this.password2,      //send username to th backend

                    //// DRF registration > expects password1 + password2
            });

            this.message ="Registration successful"
            this.$router.push("/")  //redirect to the login page
        }catch(err){
            this.message = err.response.data;
        }

    },
   },
};


</script>