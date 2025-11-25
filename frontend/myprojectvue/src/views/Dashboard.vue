<template>
  <div>
    <h2>Dashboard</h2>
    <p>{{ message }}</p> <!-- this message is coming from backend -->
  </div>
</template>

<script>
            //custom axios instance(api.js)
            //This axios instance already has your base URL (http://localhost:8000).
            //It keeps your code clean.
import api from "../axios";

export default {
  data() {
    return {
              // we will update when the API response after logging in
      message: "",
    };
  },
                //Vue automatically calls mounted() when the component is displayed.
                    //This is the best place to fetch protected data (dashboard info).

  async mounted() {
                //Your login page saved the token to localStorage.
                //Dashboard retrieves it.
                //You need this token to access Django protected API endpoints.

    const token = localStorage.getItem("access");

    try {
                            //the use of custom axios instead of this
                  //axios.get("http://localhost:8000/api/dashboard/")

                //Calls the protected endpoint /api/dashboard/
                //Django REST Framework checks:
            //IsAuthenticated → requires token authentication.
            //The token is placed inside the Authorization Header:

      const response = await api.get("/api/dashboard/", {

        headers: {

             //If the token is VALID → DRF returns the dashboard message.
             //If the token is INVALID or EXPIRED → DRF returns 401 Unauthorized.

          Authorization: `Bearer ${token}`,
        },
      });
                //updates Vue’s data with the backend response.
                //The template updates automatically.

      this.message = response.data.message;

    //If Request FAILS (401 Unauthorized)

    } catch (error) {
      this.message = "Unauthorized. Please login.";
    }
  },
};
</script>
