ymaps.ready(init);

function init() {
    // Создаем выпадающую панель с поисковыми подсказками и прикрепляем ее к HTML-элементу по его id.
    var suggestView1 = new ymaps.SuggestView('suggest1');
    var suggestView2 = new ymaps.SuggestView('suggest2');
    var suggestView3 = new ymaps.SuggestView('append1');
    var suggestView4 = new ymaps.SuggestView('append2');
}
