import AppMainPageStyles from './MainPage.module.css';

const MainPage = () => {
    return (
        <div>
            <div className={AppMainPageStyles.mainButtons}>
                <p className={AppMainPageStyles.titleNews}>Новости</p>
                <p className={AppMainPageStyles.titleIvent}>Ивенты</p>
            </div>
            <div className={AppMainPageStyles.listEvent}>
                <div className={AppMainPageStyles.listEventItem}>
                    <div>
                        <img src="/imageMainPage.svg" alt="Рамка" />
                    </div>
                    <div className={AppMainPageStyles.description}>
                        <p className={AppMainPageStyles.title}>
                            FARMA GANG STORE CABCE
                        </p>
                        <p className={AppMainPageStyles.tag}>
                            Будет
                        </p>
                        <p>
                            Лучшее что с вами происходило за последние 200 лет, объединение forma gang выступит с диджей сетом - в программе крутые ремиксы, клёвые лучшие роскошные шпашки с помидорами.

                            Диджей-сет будет проходить в формате живого выступления, где каждый момент — это уникальное музыкальное переживание. Вы сможете наблюдать за процессом создания музыки в реальном времени и стать частью этого волшебства.

                            Это событие объединит людей, которые любят музыку и ценят качественный звук.
                        </p>
                        <div className={AppMainPageStyles.bottom}>
                            <div className={AppMainPageStyles.info}>
                                <p>Клуб "Клуб"</p>
                                <p>20.07.24</p>
                            </div>
                            <div className={AppMainPageStyles.btn}>
                                <p>Подробнее</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default MainPage;
