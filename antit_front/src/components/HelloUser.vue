<template>
  <div>
    <h2>Hello, {{ username }}!</h2>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
    };
  },
  mounted() {
    this.getUsernameFromToken();
  },
  methods: {
    getUsernameFromToken() {
      const token = localStorage.getItem('access');
      try {
        if (token) {
          const decodedToken = this.parseJwt(token);
          let username = decodedToken.username
          username = username.charAt(0).toUpperCase() + username.slice(1);
          this.username = username;
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
