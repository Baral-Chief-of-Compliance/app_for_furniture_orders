<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left">Список всех товаров</div>

        <v-row class="mx-10">
            <v-col  
                cols="12"
                md="3"
            >
                <v-text-field label="Поиск товара" variant="underlined">
                </v-text-field>
                <div class="text-h5 my-5">Фильтры</div>
                <div class="text-h6 my-5">Цена</div>
                <v-radio-group>
                    <v-radio color="deep-orange" label="По возрастанию" value="1"></v-radio>
                    <v-radio color="deep-orange" label="По убыванию" value="2"></v-radio>
                </v-radio-group>
                <div class="text-h6 my-5">Поставщик</div>
                    <v-checkbox color="deep-orange" label="ООО 'Стройбат'" value="1"></v-checkbox>
                    <v-checkbox color="deep-orange" label="ООО 'SANRIKS'" value="2"></v-checkbox>
                    <v-checkbox color="deep-orange" label="ООО 'Инструментторг'" value="2"></v-checkbox>
                    <v-checkbox color="deep-orange" label="ООО 'Инструментторг'" value="2"></v-checkbox>
                    <v-checkbox color="deep-orange" label="ООО 'FIT'" value="2"></v-checkbox>
                    <v-checkbox color="deep-orange" label="ООО 'Энергомикс'" value="2"></v-checkbox>

                <div class="text-h6 my-5">Категории</div>
                    <v-checkbox color="deep-orange" label="Мебель" value="1"></v-checkbox>
                    <v-checkbox color="deep-orange" label="Электротехника" value="2"></v-checkbox>
                    <v-checkbox color="deep-orange" label="Сантехника" value="2"></v-checkbox>
                    <v-checkbox color="deep-orange" label="Инструменты" value="2"></v-checkbox>


            </v-col>

            <v-col class="mt-5">
                <v-card
                    class="my-2 pa-6 mx-14 d-flex flex-row" 
                    variant="outlined" 
                >
                    <b class="pr-2">Название:</b> Стул деревянный Калатея
                    <v-spacer></v-spacer>
                    <b class="pr-2">Поставщик:</b> ООО 'Стройбат'
                    <v-spacer></v-spacer>
                    <b class="pr-2">Категория:</b>  Мебель
                    <v-spacer></v-spacer>
                    <b class="pr-2">Цена:</b>6590 <b class="pl-2">руб.</b>
                </v-card>

                <v-card
                    class="my-2 pa-6 mx-14 d-flex flex-row" 
                    variant="outlined" 
                >
                    <b class="pr-2">Название:</b> Душевой комплект GARWELL
                    <v-spacer></v-spacer>
                    <b class="pr-2">Поставщик:</b> ООО 'Стройбат'
                    <v-spacer></v-spacer>
                    <b class="pr-2">Категория:</b>  Сантехника
                    <v-spacer></v-spacer>
                    <b class="pr-2">Цена:</b>12 397 <b class="pl-2">руб.</b>
                </v-card>

                <v-card
                    class="my-2 pa-6 mx-14 d-flex flex-row" 
                    variant="outlined" 
                >
                    <b class="pr-2">Название:</b> Встраиваемый душевой комплект 
                    <v-spacer></v-spacer>
                    <b class="pr-2">Поставщик:</b> ООО 'Стройбат'
                    <v-spacer></v-spacer>
                    <b class="pr-2">Категория:</b>  Сантехника
                    <v-spacer></v-spacer>
                    <b class="pr-2">Цена:</b>27 863 <b class="pl-2">руб.</b>
                </v-card>

            </v-col>
        </v-row>
    </v-container>
</template>

<script>

</script>