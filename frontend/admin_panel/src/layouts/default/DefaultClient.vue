<template>
    <v-app>
      <v-layout>
        <v-navigation-drawer
          expand-on-hover
          rail
          color="deep-orange"
          
        >
          <v-list>
            <v-list-item
              prepend-icon="mdi-account-tie"
              title="Admin"
              subtitle="Client@gmailcom"
            ></v-list-item>
          </v-list>
  
          <v-divider></v-divider>
  
      <v-list>
        <nav-options-client/>
      </v-list>
        </v-navigation-drawer>
  
        <v-main><default-view /></v-main>
      </v-layout>
  
      
    </v-app>
  </template>
  
  <script setup>
    import DefaultView from './View.vue'
    import NavOptionsClient from './NavOptionsClient.vue';
  </script>