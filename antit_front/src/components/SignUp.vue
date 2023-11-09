<template>
  <div>
    <h2>Sign Up</h2>
    <form @submit.prevent="signup">
      <input type="text" v-model="username" placeholder="Username" />
      <input type="password" v-model="password" placeholder="Password" />
      <button type="submit">Sign Up</button>
    </form>
    <p v-if="error" style="color: red;">{{ error }}</p>
    <p>Already have an account? <router-link to="/login">Login</router-link></p>
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
    async signup() {
      try {
        const response = await fetch('http://localhost:8000/api/signup/', {
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
