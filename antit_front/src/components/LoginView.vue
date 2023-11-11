<template>
  <div class="container mt-5">

    <div class="text-center mb-4">
      <img src="@/assets/logo.png" alt="Logo" style="max-width: 150px; max-height: 150px;" />
      <h2>AnnotateIt!</h2>
    </div>

    <div class="row justify-content-center align-items-center">
      <div class="col-md-6">
        <div class="card">
          <div class="card-body">
            <h2 class="card-title text-center mb-4">Login</h2>
            <form @submit.prevent="login">
              <div class="mb-3">
                <label for="username" class="form-label">Username</label>
                <input type="text" v-model="username" class="form-control" id="username" placeholder="Username" />
              </div>
              <div class="mb-3">
                <label for="password" class="form-label">Password</label>
                <input type="password" v-model="password" class="form-control" id="password" placeholder="Password" />
              </div>
              <button class="btn btn-primary w-100" type="submit">Login</button>
            </form>
            <p v-if="error" class="mt-3 text-danger text-center">{{ error }}</p>
            <p class="mt-3 text-center">Don't have an account? <router-link to="/signup">Sign up</router-link></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      error: null,
    };
  },
  methods: {
    async login() {
      try {
        const response = await fetch('http://localhost:8000/api/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ username: this.username, password: this.password }),
        });
        const data = await response.json();
        if (response.ok) {
          localStorage.setItem('access', data.access);
          localStorage.setItem('refresh', data.refresh);
          this.$router.push('/hello-user');
        } else {
          this.error = data.error;
        }
      } catch (error) {
        console.error('Error:', "Invalid Credentials");
        this.error = "Invalid Credentials";
      }
    },
  },
};
</script>

<style scoped>
.card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>
