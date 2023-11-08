<template>
  <div>
    <h2>Hello, {{ user.username }}!</h2>
    <router-link to="/add-audio">Add Audio</router-link>
  </div>
</template>

<script>
export default {
  name: 'HelloUser',
  data() {
    return {
      user: '',
    };
  },
  methods: {
    getUsernameFromToken() {
      const token = localStorage.getItem('access');
      try {
        if (token) {
          const decodedToken = this.parseJwt(token);
          let username = decodedToken.username
          username = username.charAt(0).toUpperCase() + username.slice(1);
          this.user = username;
        } else {
          console.error('Token is missing');
          this.$router.push('/login');
        }
      } catch (error) {
        console.error('Invalid token:', error);
        this.$router.push('/login');
      }
    },
    parseJwt(token) {
      try {
        return JSON.parse(atob(token.split('.')[1]));
      } catch (e) {
        return {};
      }
    },
  },
};
</script>
