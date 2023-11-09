<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input type="text" v-model="username" placeholder="Username" />
      <input type="password" v-model="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
    <p v-if="error" style="color: red;">{{ error }}</p>
    <p>Don't have an account? <router-link to="/signup">Sign up</router-link></p>
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
