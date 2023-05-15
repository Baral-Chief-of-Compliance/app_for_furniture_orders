<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left">Активные заказы </div>
        <v-card
                class="my-2 pa-6 mx-14 d-flex flex-row" 
                variant="outlined" 
            >
                <b class="pr-2">Название:</b> Стул деревянный Калатея
                <v-spacer></v-spacer>
                <b class="pr-2">Поставщик:</b> ООО 'Стройбат'
                <v-spacer></v-spacer>
                <b class="pr-2">Количество:</b>1  
                <v-spacer></v-spacer>
                <b class="pr-2">Цена:</b>6590 <b class="pl-2">руб.</b>
                <v-spacer></v-spacer>
                <v-btn color="deep-orange" :to="{name: 'ClientApplicationInf'}">
                    Подробно
                </v-btn>
        </v-card>
    </v-container>
</template>

<script>

</script>