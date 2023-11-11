<!-- MainPage.vue -->
<template>
    <div>
      <nav class="navbar navbar-expand-lg navbar-light bg-light  px-md-3 px-lg-4 px-xl-5">
        <router-link class="navbar-brand font-weight-bold text-success mr-auto" to="/" style="font-size: 34px;">AntIt</router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link class="nav-link" to="/hello-user">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/add-audio">Add Audio</router-link>
            </li>
          </ul>
        </div>
      </nav>
      <div class="mt-md-5">
        <slot></slot>
      </div>
    </div>
  </template>

  <script>
  import 'bootstrap/dist/css/bootstrap.min.css';
  import 'bootstrap/dist/js/bootstrap.bundle.min';

  export default {
    name: 'MainPage'
  }
  </script>
