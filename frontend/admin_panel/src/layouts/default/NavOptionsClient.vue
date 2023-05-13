<template>
    <v-list-group value="Students">
    <template v-slot:activator="{ props }">
      <v-list-item
        v-bind="props"
        prepend-icon="mdi-account-group-outline"
        title="Поставщики"
      ></v-list-item>
    </template>

    <v-list-item
      v-for="([title, icon, to], i) in categories"
      :key="i"
      :title="title"
      :prepend-icon="icon"
      :value="title"
      :to="to"
    ></v-list-item>
  </v-list-group>

  <v-list-group value="Orders">
    <template v-slot:activator="{ props }">
      <v-list-item
        v-bind="props"
        prepend-icon="mdi-package-variant-closed"
        title="Заказы"
      ></v-list-item>
    </template>

    <v-list-item
      v-for="([title, icon, to], i) in orders"
      :key="i"
      :title="title"
      :prepend-icon="icon"
      :value="title"
      :to="to"
    ></v-list-item>

    
  </v-list-group>

  <v-list-group value="Products">
    <template v-slot:activator="{ props }">
      <v-list-item
        v-bind="props"
        prepend-icon="mdi-cube-outline"
        title="Товары"
      ></v-list-item>
    </template>

    <v-list-item
      v-for="([title, icon, to], i) in products"
      :key="i"
      :title="title"
      :prepend-icon="icon"
      :value="title"
      :to="to"
    ></v-list-item>

    
  </v-list-group>

</template>

<script>
  export default {
    data: () => ({
      categories: [
        ['Список', 'mdi-account-multiple', '/client/providers']
      ],
      orders:[
        ['Список', 'mdi-animation', '/teachers']
        // ['Оформить', 'mdi-package-variant', '/teachers']
      ],
      products:[
        ['Список', 'mdi-cube-unfolded', '/teachers']
      ],
    }),
  }
</script>