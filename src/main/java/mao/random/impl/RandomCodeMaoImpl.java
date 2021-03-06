package mao.random.impl;

import main.java.core.annotation.Mao;
import main.java.core.vo.RandomCodeVO;
import main.java.mao.random.IRandomCodeMao;
import org.mongodb.morphia.Datastore;
import org.mongodb.morphia.DatastoreImpl;

/**
 * Created by digvijaysharma on 15/01/17.
 */
@Mao
public class RandomCodeMaoImpl implements IRandomCodeMao{

    private Datastore store;

    public RandomCodeMaoImpl(DatastoreImpl store) {
        this.store = store;
    }

    @Override
    public RandomCodeVO getRandomCodeByCode(String code) {
        return store.find(RandomCodeVO.class, "code", code).get();
    }

    @Override
    public void createRandomCode(RandomCodeVO randomCode) {
        store.save(randomCode);
    }
}
